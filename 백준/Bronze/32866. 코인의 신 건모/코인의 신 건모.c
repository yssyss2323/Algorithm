#include <stdio.h>

int main() {
    double n, x;
    scanf("%lf %lf", &n, &x);

    double ans = (100 / (100 - x) - 1) * 100;
    printf("%lf", ans);
    return 0;
}