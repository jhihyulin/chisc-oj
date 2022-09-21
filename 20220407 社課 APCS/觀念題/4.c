#include<stdio.h>

int main(){
    int i, sum, arr[10];
    for (int i=0; i<10; i++)
        arr[i] = i;
    sum = 0;
    for (i=1; i<9; i++)
        sum = sum - arr[i-1] + arr[i] +arr[i+1];
    printf("%d\n", sum);
}