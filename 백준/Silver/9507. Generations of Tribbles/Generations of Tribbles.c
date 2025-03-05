#include <stdio.h>
#define MAX 67

int main() {
    int t;
    scanf("%d", &t);

    long long int dp[MAX + 1];
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for (int i = 4; i< MAX + 1; i++){
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4];
    }
    
    for (int i = 0; i < t; i++){
        int curr;
        scanf("%d", &curr);
        printf("%lld\n", dp[curr]);
    }
    return 0;
}