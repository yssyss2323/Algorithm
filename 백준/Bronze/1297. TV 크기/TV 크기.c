#include <stdio.h>
#include <math.h>

int main() {
    int d, h, w;
    scanf("%d %d %d", &d, &h, &w);

    int real_h = h * d / sqrt(h * h + w * w);
    int real_w = w * d / sqrt(h * h + w * w);
    printf("%d %d", real_h, real_w);
    return 0;
}