#include <stdio.h>

int main(){
    int cost;
    scanf("%d", &cost);
    cost = 1000 - cost;

    int ans = 0;
    int coins[] = {500, 100, 50, 10, 5, 1};
    int n = sizeof(coins) / sizeof(coins[0]);

    int* p;
    for (p = &coins[0];p < &coins[n];p++){
        ans += cost / *p;
        cost = cost % *p;
    }

    printf("%d", ans);
    
}