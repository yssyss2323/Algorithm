#include <stdio.h>

int main() {
    int n, p;
    scanf("%d %d", &n, &p);

    int ans = p;
    if (n >= 5) {
        ans -= 500;
    }
    if (n >= 10) {
        if (ans > p * 0.9) ans = p * 0.9;
    }
    if (n >= 15) {
        if (ans > p - 2000) ans = p - 2000;
    }
    if (n >= 20) {
        if (ans > p * 0.75) ans  = p * 0.75;
    }
    if (ans < 0) ans = 0;
    printf("%d", ans);
    return 0;
}