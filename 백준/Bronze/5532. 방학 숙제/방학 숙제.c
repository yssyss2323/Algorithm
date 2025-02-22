#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))

int calc(int x, int y){
    int ans = x / y;
    if (x % y > 0) ans++;

    return ans;
}

int main() {
    int l, a, b, c, d;
    scanf("%d %d %d %d %d", &l, &a, &b, &c, &d);
    
    printf("%d\n", l - MAX(calc(a, c), calc(b, d)));
    return 0;
}