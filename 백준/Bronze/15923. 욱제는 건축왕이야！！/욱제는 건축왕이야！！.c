#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    int x, y;
    scanf("%d %d", &x, &y);
    int tmpx = x, tmpy = y;
    
    int ans = 0;
    for (int i = 0; i < n - 1; i++) {
        int tmpxx, tmpyy;
        scanf("%d %d", &tmpxx , &tmpyy);

        ans += abs(tmpxx - tmpx) + abs(tmpyy - tmpy);
        tmpx = tmpxx;
        tmpy = tmpyy;
    }

    ans += abs(x - tmpx) + abs(y - tmpy);

    printf("%d", ans);
    return 0;
}