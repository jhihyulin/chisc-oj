#include<stdio.h>

int main(){
    int a=5;

    for (int i=0; i<20; i++) {
        i = i + a;
        printf("%d\n", i);
    }
}