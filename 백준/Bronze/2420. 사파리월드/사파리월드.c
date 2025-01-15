#include <stdio.h>

int main() {
    long long int n, m, ans;
    scanf("%lld %lld", &n, &m);
    if (n >= m) ans = n - m;
    else ans = m - n;
    printf("%lld", ans);
    return 0;
}