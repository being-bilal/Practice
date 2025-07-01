#!/usr/bin/env python3
"""
DualShock Controller Monitor for Raspberry Pi
Displays real-time input from connected DualShock controller
"""

import pygame
import sys
import time

def initialize_pygame():
    """Initialize pygame and joystick modules"""
    pygame.init()
    pygame.joystick.init()
    
    # Check if any joysticks are connected
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No controllers found!")
        return None
    
    print(f"Found {joystick_count} controller(s)")
    
    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    print(f"Controller: {joystick.get_name()}")
    print(f"Axes: {joystick.get_numaxes()}")
    print(f"Buttons: {joystick.get_numbuttons()}")
    print(f"Hats: {joystick.get_numhats()}")
    print("-" * 50)
    
    return joystick

def format_axis_value(value, threshold=0.1):
    """Format axis values with dead zone"""
    if abs(value) < threshold:
        return 0.0
    return round(value, 3)

def main():
    joystick = initialize_pygame()
    if not joystick:
        sys.exit(1)
    
    clock = pygame.time.Clock()
    
    # DualShock button mapping (may vary by model)
    button_names = {
        0: "X", 1: "Circle", 2: "Square", 3: "Triangle",
        4: "L1", 5: "R1", 6: "L2", 7: "R2",
        8: "Share", 9: "Options", 10: "L3", 11: "R3",
        12: "PS", 13: "Touchpad"
    }
    
    # Axis mapping for DualShock
    axis_names = {
        0: "Left X", 1: "Left Y",
        2: "Right X", 3: "Right Y",
        4: "L2 Trigger", 5: "R2 Trigger"
    }
    
    print("Press Ctrl+C to exit\n")
    
    try:
        while True:
            pygame.event.pump()
            
            # Clear screen (works on most terminals)
            print("\033[2J\033[H", end="")
            
            print("DualShock Controller Status")
            print("=" * 40)
            
            # Display button states
            print("BUTTONS:")
            pressed_buttons = []
            for i in range(joystick.get_numbuttons()):
                if joystick.get_button(i):
                    button_name = button_names.get(i, f"Button {i}")
                    pressed_buttons.append(button_name)
            
            if pressed_buttons:
                print(f"  Pressed: {', '.join(pressed_buttons)}")
            else:
                print("  None pressed")
            
            print()
            
            # Display joystick values with enhanced detail
            print("JOYSTICK VALUES:")
            
            # Left stick
            left_x = format_axis_value(joystick.get_axis(0))
            left_y = format_axis_value(joystick.get_axis(1))
            left_magnitude = (left_x**2 + left_y**2)**0.5
            
            print(f"  Left Stick:")
            print(f"    X: {left_x:6.3f}  Y: {left_y:6.3f}  Magnitude: {left_magnitude:.3f}")
            
            # Right stick
            right_x = format_axis_value(joystick.get_axis(2))
            right_y = format_axis_value(joystick.get_axis(3))
            right_magnitude = (right_x**2 + right_y**2)**0.5
            
            print(f"  Right Stick:")
            print(f"    X: {right_x:6.3f}  Y: {right_y:6.3f}  Magnitude: {right_magnitude:.3f}")
            
            print()
            print("TRIGGERS:")
            for i in range(4, min(6, joystick.get_numaxes())):
                value = format_axis_value(joystick.get_axis(i))
                axis_name = axis_names.get(i, f"Axis {i}")
                
                # Create a trigger bar (0 to 1 instead of -1 to 1)
                trigger_val = (value + 1) / 2  # Convert -1,1 to 0,1
                bar_length = 20
                filled = int(trigger_val * bar_length)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                print(f"  {axis_name:12}: {trigger_val:5.3f} [{bar}] {int(trigger_val*100):3d}%")
            
            print()
            print("ALL AXES (Raw Values):")
            for i in range(joystick.get_numaxes()):
                value = format_axis_value(joystick.get_axis(i))
                axis_name = axis_names.get(i, f"Axis {i}")
                print(f"  {axis_name:12}: {value:6.3f}")
            
            print()
            
            # Display D-pad (hat) status
            print("D-PAD:")
            if joystick.get_numhats() > 0:
                hat = joystick.get_hat(0)
                dpad_state = "Center"
                
                if hat[0] == -1:
                    dpad_state = "Left"
                elif hat[0] == 1:
                    dpad_state = "Right"
                
                if hat[1] == 1:
                    if dpad_state == "Center":
                        dpad_state = "Up"
                    else:
                        dpad_state += "-Up"
                elif hat[1] == -1:
                    if dpad_state == "Center":
                        dpad_state = "Down"
                    else:
                        dpad_state += "-Down"
                
                print(f"  Direction: {dpad_state}")
            else:
                print("  No D-pad detected")
            
            print()
            print("Press Ctrl+C to exit")
            
            # Update at 30 FPS
            clock.tick(30)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
