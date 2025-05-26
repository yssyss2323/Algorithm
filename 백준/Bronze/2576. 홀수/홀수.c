#include <stdio.h>

int main() {
    int nums[7];
    int tot = 0;
    int min = 100;
    for (int i = 0; i < 7; i++) {
        scanf("%d", &nums[i]);
        if (nums[i] % 2 == 1) {
            tot += nums[i];
            if (min > nums[i]) min = nums[i];
        }
    }
    if (min == 100) printf("%d", -1);
    else {
        printf("%d\n", tot);
        printf("%d", min);   
    }
    return 0;
}