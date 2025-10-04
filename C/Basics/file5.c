# include <stdio.h>
# include <ctype.h>

int main(){
    // Arrays
    float array1[5] = {2.45, 6.7, 7.32}; // the remaining two elements would be assigned as 0
    printf("%f \n", array1[4]);
    char array2[5] = {'v', 'h', 'r'}; // the remaining two elements would be assigned as null
    int array3[10] = {0}; // array of 10 zeros
    char string[] = "hello World"; // the last element of the string is null \0
    printf("%c \n", string[10]); // returns d
    string[0] = 'H';
    printf("%s \n", string);

    // length of the array 
    int len = sizeof(string)/sizeof(string[0]);
    printf("length of array : %d \n", len);

    // printing an array
    for(int i=0; i<len; i++){
        printf("array[%d] : %c \n", i, string[i]);
    }
    // multi-dimensional array
    int array_2d[3][4] = {
        {4,6,7,2},
        {3,7,8,4},
        {3,5,7,6}
    };
    int row = sizeof(array_2d)/sizeof(array_2d[0]);
    int column = sizeof(array_2d[0])/sizeof(array_2d[0][0]);
    printf("dimension of array : %d x %d \n", row, column);
    return 0;

}