#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    if ((n * m) % 3 == 0) printf("YES");
    else printf("NO");
    return 0;
}