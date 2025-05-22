# include <iostream>
using namespace std;

int main(){
    // Taking Input from the user 
    char grade;
    double cgpa;
    string name; // string cannot use cin directly thus it uses getline to take input
    cout << "Input the following Data" << endl << "Grade : ";
    cin >> grade;
    cout << "CGPA : ";
    cin >> cgpa;

    cin.ignore();  // This clears the newline left by previous `cin`
    
    // Taking String as an Input 
    cout << "Enter your name : ";
    getline(cin, name); 
    cout << "Your name is " << name << endl;
    return 0;
}