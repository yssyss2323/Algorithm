#include <stdio.h>

int main() {
    int a,b;
    scanf("%d %d", &a, &b);
    int ans = 2;
    while(a > 2){
        int tmp = a;
        a = b;
        b = tmp - 1;
        ans += 1;
    }
    printf("%d", ans);
    return 0;
}