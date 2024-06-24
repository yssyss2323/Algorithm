#include <stdio.h>

int main() {
    int x,y,w,h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    int ans;
    int tmp1, tmp2;
    if (x < w-x) tmp1 = x;
    else tmp1 = w-x;
    if (y < h-y) tmp2 = y;
    else tmp2 = h-y;
    if (tmp1 < tmp2) ans = tmp1;
    else ans = tmp2;
    printf("%d", ans);
    return 0;
}