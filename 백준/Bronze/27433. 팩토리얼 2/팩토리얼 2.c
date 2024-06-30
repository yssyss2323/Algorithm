#include <stdio.h>

long recur(int x){
    if (x == 0) return 1;
    return x * recur(x-1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%ld", recur(n));
    return 0;
}