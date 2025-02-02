#include <stdio.h>

void sort(int arr[], int len){
    for (int i = 0; i < len; i++){
        for (int j = i; j < len; j++){
            if (arr[i] > arr[j]){
                int tmp = arr[j];
                arr[j] = arr[i];
                arr[i] = tmp;
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        int nums[10];
        for (int j = 0; j < 10; j++){
            scanf("%d", &nums[j]);
        }
        sort(nums, 10);
        printf("%d\n", nums[7]);
        
    }
    return 0;
}