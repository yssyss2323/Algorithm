#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long int tot = 0;
    for (int i = 0; i < n * n; i++) {
        int tmp;
        scanf("%d", &tmp);

        tot += tmp;
    }
    printf("%lld", tot);
    return 0;
}