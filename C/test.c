
#include <stdio.h>

int is_prime(int num) {
    // from numbers smaller or equal to 1 
    if (num <= 1){
        return 0; 
    }
    // from numbers greater or equal to 2
    for (int i = 2; i < (num/2); i++) {
        if (num % i == 0) 
            return 0; 
    }
    return 1; // Prime
}

int main() {
    int number;

    // Taking input
    printf("Enter an number : ");
    scanf("%d", &number);

    // Checking and printing result
    if (is_prime(number)){
        printf("%d is a prime number.\n", number);
    }
    else{
        printf("%d is not a prime number.\n", number);
    }
        

    return 0;
}

