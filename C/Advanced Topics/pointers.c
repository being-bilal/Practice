# include <stdio.h>

void add1(int *n){
    *n = (*n + 1);
}

int main(){
    // Pointers : pointers are variables that store the memory address of another variable and access their value by dereferencing the pointer.
    int a = 10;
    int *b; // pointer variable declaration (the type of the pointer must match the type of the variable it points to)
    b = &a; // & gives the address of the variable 
    printf("The address of a is %p\n", b);
    printf("The value of a is %d \n", *b); // * is used to dereference the pointer and access the value at that address
    printf("The value of b is %p \n", &b);


    // Pointer Arithmetic
    // incrementing a pointer increases its value by the size of the data type it points to
    printf("value of b before increment:  %p\n", b);
    printf("value b stores : %d\n", *b);
    b += 1;
    printf("value of b after increment:  %p\n", b); // since a is a int (4 bytes), b is incremented by 4
    printf("value b stores : %d\n", *b); // garbage value

    // Pointer Types (changing pointer types using typecasting)
    int var = 1025;
    int *ip = &var; // int pointer (takes 4 bytes)
    char *ch = "Hello"; // char pointer (takes 1 byte)
    printf("Value of ip = %p, value stored in ip = %d\n", ip, *ip);
    ch = (char*)ip; // typecasting int pointer to char pointer
    printf("Value of ch = %p, value stored in ch = %d\n", ch, *ch);


    // Pointer to Pointer
    // it is a pointer variable that stores the address of another pointer variable and can be used to access the value of the original variable by dereferencing twice.
    int x = 5; 
    int *p1 = &x;
    int **p2 = &p1; // p2 is a pointer to the int pointer p1
    int ***p3 = &p2; // p3 is a pointer to the pointer to the int pointer p1
    printf("Value of x = %d\n", x);
    printf("Value of x using p1 = %d\n", *p1);
    printf("Address of p1 = %d, value of p1 = %d, value of x using p2 = %d\n", p2, *p2, **p2);
    ***p3 = 20; // changing the value of x using p3
    printf("Value of x = %d\n", x);


    // Pointers as function arguments (call by reference)
    // passing the address of a variable to a function allows the function to modify the original variable's value

    int n = 10;
    printf("Value of n before function call: %d\n", n);
    int *ptr = &n;
    add1(ptr);
    printf("Value of n after function call: %d\n", n);

    // Pointers and Arrays 
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr; // the array pointer points to the address of the first element of the array 
    printf("address of the first element of array : %p\n", p);
    printf("First element of array using pointer : %d\n", *p);


    return 0;
}

