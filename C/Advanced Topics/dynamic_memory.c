#include <stdio.h>
# include <stdlib.h> // for malloc and free
int main(){
    if(1){
        int *p = (int *)malloc(5 * sizeof(int)); // dynamically allocate memory for 5 integers
        for(int i = 0; i < 5; i++){
            p[i] = i + 1; // assign values to the allocated memory
        }
        printf("Dynamically allocated array: ");
        for(int i = 0; i < 5; i++){
            printf("%d ", p[i]); // print the values
        }
        printf("\n");
        free(p); // free the allocated memory
    } else {
        int arr[5]; // statically allocate memory for 5 integers
        for(int i = 0; i < 5; i++){
            arr[i] = i + 1; // assign values to the array
        }
        printf("Statically allocated array: ");
        for(int i = 0; i < 5; i++){
            printf("%d ", arr[i]); // print the values
        }
        printf("\n");
    }
    return 0;
}
