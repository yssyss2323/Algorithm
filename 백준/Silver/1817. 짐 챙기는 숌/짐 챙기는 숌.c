#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int ans = 1;
    int margin = m;
    int now;
    for (int i = 0; i < n; i++){
        scanf("%d", &now);
        if (margin >= now) margin -= now;
        else {
            margin = m - now;
            ans += 1;
        }
    }
    if (n == 0) printf("0");
    else printf("%d", ans);
    return 0;
}