#include <stdio.h>

int main() {
    int n, x;
    scanf("%d %d", &n, &x);

    int cost[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &cost[i]);
    }

    int ans = 2000;
    for (int i = 0; i < n - 1; i++) {
        if (cost[i] + cost[i + 1] < ans) ans = cost[i] + cost[i + 1];
    }

    printf("%d", ans * x);
    
    return 0;
}