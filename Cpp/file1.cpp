// These first two lines are called directives
//preprocessor directive are the instructions to the complier to execute certain commands before the compilation starts
#include <iostream> // preprocessor directive
using namespace std; // using directive

int main(){
    // Variables
    string name; // declaring a string variable
    name = "Bilal"; // assigning value to a string variable
    int num1 = 10, num2 = 20;
    int num3, num4, num5;
    num3 = num4 = num5 = 30; // multi variable assignment
    int age; // Initialising the variable 
    age = 19; // defining the variable  
    cout << "My name is " << name << ", I was " << age << " years old in 2024" << endl;
    age = 20; // Changing the variable value 
    cout << "Now i am " << age << " years old" << endl;

    // Difference between "\n" and endl:
    // '\n' It tells the program to “insert a line break here”.
    // whereas, endl is a C++ manipulator that creates a new line and flushes the output buffer
    return 0;
}
