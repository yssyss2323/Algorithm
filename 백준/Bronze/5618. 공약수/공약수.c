#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int n;
    scanf("%d", &n);

    int nums[3];
    scanf("%d %d %d", &nums[0], &nums[1], &nums[2]);
    
    int max_cd = nums[0];
    for (int i = 1; i < n; i++) {
        max_cd = gcd(max_cd, nums[i]);
    }

    int divisors[20000];
    int cnt = 0;

    for (int i = 1; i <= sqrt(max_cd); i++) {
        if (max_cd % i == 0) {
            divisors[cnt++] = i;
            if (i != max_cd / i) {
                divisors[cnt++] = max_cd / i;
            }
        }
    }

    qsort(divisors, cnt, sizeof(int), compare);
    printf("%d", divisors[0]);
    for (int i = 1; i < cnt; i++){
        printf("\n%d", divisors[i]);
    }
    
    return 0;
}