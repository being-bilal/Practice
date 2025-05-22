# include <iostream>
using namespace std;

int main(){
    // Working with the Strings
    string str = "Hello World";
    string str("Hello World");

    cout << "This is a string" << endl; // endl is used to create a new line which can also be done using "\n"
    cout << "this is also a string \n";
    
    // Length of the string 
    cout << str.length() << endl; // returns the number of chars in a string 
    
    // String indexing 
    cout << str[1] << endl;
    str[5] = '_'; // changing the value of char in string 
    cout << str << endl;
    cout << str.find("lo") << endl; // returns the index of the first occurance of the given string  

    // SubString
    string str2 = str.substr(3, 5); // substr(start_index, length of substring)
    string str3 = str.substr(str.length() - 3, 3);  // Accessing the last 3 chars
    cout << str3 << endl;

    return 0;
}