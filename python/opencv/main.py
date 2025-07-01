import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('(\d+)', s)]

image_dir = 'python/opencv/images'
images = sorted(os.listdir(image_dir), key=natural_sort_key)

with open('python/opencv/pairs.txt', 'w') as f:
    for i in range(len(images) - 1):
        f.write(f"{images[i]} {images[i+1]}\n")
