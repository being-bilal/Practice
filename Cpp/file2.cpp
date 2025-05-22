# include <iostream>
using namespace std;

int main(){
    // DataTypes
    char Grade = 'A'; 
    string name = "Mohhd Bilal";
    int age = 20; // Takes 4 bytes of memory
    long number = 5787578943564387; // long is a integer DataType with larger range than int
    float cgpa = 7.86; // Used to store floating point values (takes 4 bytes)
    double gpa = 8.646; // double is a floating point DataType with double precision (takes 8 Bytes)
    long double pi = 3.141592653589793; // Even higer precision then double (takes 16 bytes)
    bool passed = true; 
    
    cout << sizeof(float) << endl;
    return 0; 
}