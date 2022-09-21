#include<stdio.h>

int main(){
    int a=0, n=2;

    for (int i=1; i<=n; i++)
        for (int j=i; j<=n; j++)
            for (int k=1; k<=n; k++)
                a++;
            
    printf("%d\n", a);
}