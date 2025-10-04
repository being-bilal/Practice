# include <stdio.h>

#define PI 3.14 // define is a preprocessor compiler directive

int main(){
    // DataTypes
    typedef int unit; // now int keyword can be replaced by unit 
    printf("hello \n");
    const int num = 100UL; // constant unsigned large integer 
    float num2 = +.5e-2; // real number 
    unit num3 = 20;
    char char1 = 'A';
    volatile int num4 = 10; // can be changed by both an external program and the parent program
    volatile const int num5 = 15; // can only be chnaged by an external program
    printf("%d \n", char1); // returns the ASCII value of char 
    printf("%2.2f \n", num2);
    printf("%d \n", num3);
    printf("Size of int: %lu\n", sizeof( long double));  

    // enum 
    enum weekdays {
        MON, TUE, WED, THU, FRI, SAT, SUN
    }; // creates user defined datatype 
    enum weekdays today = MON;
    printf("%d", today); // return 2
    return 0;
}
