# include <stdio.h>
# include <ctype.h>

int main(){
    // Loops 
    // 1) Entry controlled loops : for loops(counter based), while loops(sentinal based control)
    // 2) Exit controlled loops : do loops

    // while loop
    int num = 0;
    while(num < 10){
        printf("%d \n", (num*num));
        if ((num*num)%2 ==0) goto even; //use of goto statement
        else goto odd;

        even:
            printf("%d is even \n", (num*num));
            num++;
            continue; // using continue otherwise the odd block would  also be executed 
        odd: 
            printf("%d is odd \n", (num*num));
            num++;

    }
    // Do-loop
    do{
        printf("num : %d \n", num);
    }while(num > 100);

    // For loop
    for(int i=5; i >= 0; --i){
        printf("%d \t", i);
    }
    // Multi variable For-loop
    int n,m;
    for(int n = 0, m = 10; n < 10; n++, m-- ){
        printf("n : %d, m : %d, m+n : %d \n", n,m,(n+m));
    }
    // single section for-loop
    int x = 100;
    for( ; x > 10 ; ){ //must have the semicolon of initialising, and increment sectiions even if they are not used 
        printf("x : %d \n", x);
        if (x == 50){
            printf("x is equal to 50, breaking from loop \n");
            break;
        }
        x -= 10;
    }
    

    return 0;
}