#include <stdio.h>
#include <ctype.h>

// function declaration
void printLine(void);

// Function with arguments but no return value 
void customLine(char symbol){
    for(int i=0; i < 60; i++){
        printf("%c", symbol);
    }
    printf("\n");
}

// Function with arguments and a return value
float Average(int a, int b){
    int avg = (a + b)/2;
    return avg;
}

// Function with aarguments and pointer(output variable) 
float calc(int a, int b, int *sum, int *product){
    *sum = a+b;
    *product = a*b;
}

// Recursion 
int factorial(int n){
    // automatic variable are local variable that are destroyed after the function has finished executing
    auto int fact; 
    if(n==1 || n==0){
        fact = 1;
    }else{
        fact = n*factorial(n-1);
    }
    return fact;
} 

int main(){
    // Functions   
    printf("Hello \n");
    printLine(); // function call
    printf("World \n");
    customLine('#');
    printf("Average = %.2f \n", Average(34, Average(56,73)));
    int x=10, y=30, s, p;
    calc(x, y, &s, &p);
    printf("sum = %d, product = %d \n", s, p);
    printf("5! : %d \n", factorial(5));
    return 0;
}

// function defination
void printLine(void){
    for(int i=0; i < 60; i++){
        printf(".");
    }
    printf("\n");
}

