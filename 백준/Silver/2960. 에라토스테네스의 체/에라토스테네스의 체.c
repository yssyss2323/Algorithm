#include <stdio.h>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int num[n + 1];
    num[0] = 0;
    num[1] = 0;
    for (int i = 2; i < n + 1; i++){
        num[i] = 1;
    }

    int ans = 0;
    for (int i = 2; i < n + 1; i++){
        for (int j = i; j < n + 1; j += i){
            if (num[j] == 1){
                num[j] = 0;
                k--;
            }
            if (k == 0) {
                ans = j;
                printf("%d", ans);
                break;
            }
        }
        if (ans > 0) break;
    }
    return 0;
}