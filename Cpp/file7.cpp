# include <iostream>
using namespace std;

// declaring and Defining a function 
void add(int a = 0, int b = 0){ // void is used when the function is not supposed to return any value
    cout << "sum of " << a << " and " << b << " is "<< a+b << endl; 
}
// declaring a function without defining it 
int max(int a, int b);

string greeting(string name){
    string val = "Goodmorning " + name;
    return val;
}

int firstElement(int list[]){
    return list[0];
}


int main(){
    // Functions
    int num1 = 100;
    int num2 = 50;
    int list1[] = {3,3,5,5,7,8,8,9,3,7,32,2};
    // calling the function 
    add(num1, num2);
    add(100); 
    int num3 = max(num1, num2); // assigning the return value of function to a variable 
    cout << num3 << endl; 
    cout << greeting("Bilal") << endl;
    cout << firstElement(list1) << endl;
    return 0;
}

int max(int a, int b){
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}