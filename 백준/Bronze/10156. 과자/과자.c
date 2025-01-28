#include <stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    int ans = 0;
    if (a * b - c > ans) ans = a * b - c;
    printf("%d", ans);
}