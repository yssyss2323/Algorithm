#include <stdio.h>

long fibo(int x){
    if (x == 0) return 0;
    if (x == 1) return 1;
    if (x == 2) return 1;
    return fibo(x - 1) + fibo(x - 2);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%ld", fibo(n));
    return 0;
}