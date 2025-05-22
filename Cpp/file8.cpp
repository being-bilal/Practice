# include <iostream>
using namespace std;

int calc(int a, int b, char operation){
    if (a < 0 or b < 0){ // Nested If-else statement
        cout << "Please choose positive values only" << endl;
    }
    else{ 
        if (operation == 'A'){
            return a+b;
        }
        else if (operation == 'S'){
            return a-b;
        }
        else{
            cout << "Invalid Operation Character" << endl;
        }
    }
    return 0;
}


int main(){
    // Conditionals (IF ELLSE statement)
    int num = 100;
    if (num >= 10){
        cout << "number is greater or equal to 10" << endl;
    }else{
        cout << "number is smaller than 10" << endl;
    }
    cout << calc(20, -50, 'S') << endl;

    // switch Statement 
    int num1, num2;
    char operation;
    cout << "Choose 1st number : ";
    cin >> num1;
    cout << "Choose 2nd number : ";
    cin >> num2;
    cout << "Choose choose the operation: ";
    cin >> operation;

    switch (operation){
        case '+':
            cout << num1 + num2 << endl;
            break; // Breaks aways from the switch statement, without break all the cases would be executed
        case '-':
            cout << num1 - num2 << endl;   
            break;
        case '*':
            cout << num1 * num2 << endl;
            break;
        case '/':
            cout << num1 / num2 << endl;
            break;
        default:
            cout << "Invalid Operation!!" << endl;
    }

    // 
    
    return 0;
}