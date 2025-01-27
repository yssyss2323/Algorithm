#include <stdio.h>

int main(){
    int a, b, c, d, e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    int ans = -50;
    if (a < b){
        if (a < c) ans += a;
        else ans += c;
    }
    else {
        if (b < c) ans += b;
        else ans += c;
    }
    if (d < e) ans += d;
    else ans += e;
    printf("%d", ans);
}