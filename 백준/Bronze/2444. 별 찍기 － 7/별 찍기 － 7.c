#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    for (int i=0; i<a; i++){
        for (int j=0; j<a-1-i;j++){
            printf(" ");
        }
        for (int j=0; j<i*2+1;j++){
            printf("*");
        }
        printf("\n");
    }
    for (int i=0; i<a-1; i++){
        for (int j=0; j<i+1;j++){
            printf(" ");
        }
        for (int j=0; j<a*2-1-2*(i+1);j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}