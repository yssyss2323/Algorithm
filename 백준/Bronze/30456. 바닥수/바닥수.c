#include <stdio.h>

int main() {
    int n, l;
    scanf("%d %d", &n, &l);

    long long int ans = 1;
    for (int i = 0; i < l - 2; i++){
        ans *= 10;
        ans += 1;
    }
    ans = ans * 10 + n;
    printf("%lld", ans);
    return 0;
}