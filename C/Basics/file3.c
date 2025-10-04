# include <stdio.h>
# include <ctype.h>

#include <stdio.h>

int main() {
    int num1, num2;

    printf("Enter two numbers:\n");
    printf("Number-1: ");
    scanf("%d", &num1);

    printf("Number-2: ");
    scanf("%d", &num2);

    // if statement 
    if (num1 + num2 > 10) {
        float ratio = (float)num1 / (float)num2;
        printf("Ratio: %.2f\n", ratio);  
    }

    // switch statement
    switch (num1+num2) // value checked using switch should integral type 
    {
    case 10:
        printf("Sum is 10 \n");
        break;
    case 100:
        printf("Sum is 100 \n");
        break;
    case 1000:
        printf("Sum is 100 \n");
        break;
    
    default:
        break;
    }
    // ternary operator as conditional 
    int sum = num1 + num2;
    char check = (sum != 0 ? ((sum > 0) ? 'P' : 'N') : 'Z');
    printf("%c \n", check);
    return 0;
}
