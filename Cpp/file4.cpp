# include <iostream>
# include <cmath> // used to do advanced math operations

using namespace std;

int main(){
    // Working with Numbers 
    int num1 = 10;
    int num2 = 3;

    // In C++ the operation done on integers always returns an int and not a float even in case of division 
    cout << num1/num2 << endl;  // does floor division if the numbers are int
    cout << 10.0/3.0 << endl; // does actual divison if numbers are float
    
    // CMath functions 
    cout << pow(2, 6) << endl; // raise number to a specified power
    cout << fmax(3.9, 3.11) << endl; // returns the max value between two ints
    cout << round(2.45) << endl;
    cout << ceil(2.4) << endl;

    // Incrementing the number by one
    num2++; // post increment 
    ++num2; // pre increment 
    cout << num2 << endl;
    int num3 = ++num2; //increment the num2 by one and then set it to num3 
    num2 = 5;
    int num4 = num2++; // sets the num4 equal to num2 then increments the value of num2
    cout << "num3:" << num3 << " num4:" << num4 << endl;
    cout << "num2 : " << num2 << endl;

    return 0;
}