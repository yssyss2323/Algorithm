#include <stdio.h>
#define PI 3.141592

int main() {
    int d1, d2;
    scanf("%d %d", &d1, &d2);
    float ans = 2 * (d1 + d2 * PI);
    printf("%f", ans);
    return 0;
}