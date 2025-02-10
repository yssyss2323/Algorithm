#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int nums[n];
    long long int tot1 = 0, tot2 = 0;
    for (int i = 0; i < n; i++){
        scanf("%d", &nums[i]);
        tot1 += (nums[i] / 30 + 1) * 10;
        tot2 += (nums[i] / 60 + 1) * 15;
    }
    if (tot1 < tot2) printf("Y %lld", tot1);
    else if (tot1 > tot2) printf("M %lld", tot2);
    else printf("Y M %lld", tot1);
    return 0;
}