#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int xmin = 10000, xmax = -10000, ymin = 10000, ymax = -10000;

    for (int i = 0; i < n; i++){
        int x,y;
        scanf("%d %d", &x, &y);
        if (x < xmin) xmin = x;
        if (xmax < x) xmax = x;
        if (y < ymin) ymin = y;
        if (ymax < y) ymax = y;
    }
    printf("%d", (xmax - xmin) * (ymax - ymin));
    return 0;
}