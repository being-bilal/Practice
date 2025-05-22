# include <stdio.h>

int main(){
    // Operators and Expressions
    int x = 10;
    int y = ++x; //increments x to 11 and then assigns  it to y
    printf("x : %d, y: %d \n", x, y); 
    int z = x++; // assigns the value of x(11) to z and then increments it to 12
    printf("x : %d, z: %d \n", x, z); 

    // comma operator 
    int a,b;
    int value = (a = 10, b = 20, a+b);
    printf("%d \n", value);

    // ternary operator
    int val = (value%2 == 0) ? 1 : 0;
    printf("%d \n", val);

    return 0;
}