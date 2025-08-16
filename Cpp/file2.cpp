# include <iostream>
# include <cmath>
using namespace std;

# define e 2.718281828459045 // constants can be defined using preprocessor directive
int main(){
    // DataTypes
    const long double PI = 3.141592653589793;
    cout << PI << endl; // value of pi cant be changed in the program as it is a constant
    char Grade = 'A'; 
    string name = "Mohhd Bilal";
    int age = 20; // Takes 4 bytes of memory
    cout << "bytes taken 'by int' datatype : " << sizeof(int) << " Bytes"<< endl;
    long number = 5787578943564387; // long is a integer DataType with larger range than int
    float cgpa = 7.86; // Used to store floating point values (takes 4 bytes)
    double gpa = 8.34E-5; // double is a floating point DataType with double precision (takes 8 Bytes)
    long double pi = 3.141592653589793; // Even higer precision then double (takes 16 bytes)
    bool passed = true;

    cout << sizeof(int) << endl;

    // By assigning unsigned to a variable we can extend their range to only hold positive numbers
    // they can represent positive numbers twice as big as the signed int can
    unsigned int num = 3043905;
    cout << sqrt(num) << endl;
    return 0; 
}