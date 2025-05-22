# include <iostream>
using namespace std;

int main(){
    // Arrays 
    // data_type array_name[Size_of_array] = {};
    int array[6] = {1,3,5,7,9,11};
    int array2[] = {3,5,7,8,5,2,7,9,3,7,9,4}; // array without defining the size of it
    char char_array[] = "mohd Bilal"; // char array
    cout << array2[0] << endl; //Accessing the first element of the array

    char_array[0] = 'M'; // changing the value of the array
    cout << char_array << endl; 

    // finding the number of elements in a array
    int total_size = sizeof(array2);
    int element_size = sizeof(array2[0]);
    cout << "Length of the array is : "<< total_size/element_size << endl;

    // 2D array
    int arr[3][4] = {
        {1,2,4,6},
        {2,5,7,8},
        {2,6,7,2}
    };
    cout << arr[0][2] << endl;

}