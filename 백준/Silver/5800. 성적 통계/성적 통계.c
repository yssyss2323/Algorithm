#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    return (*(int*) a - *(int*) b);
}

int main() {
    int k;
    scanf("%d", &k);
    for (int i = 0; i < k; i++){
        printf("Class %d\n", i + 1);

        int n;
        scanf("%d", &n);

        int arr[n];
        for (int j = 0; j < n; j++){
            scanf("%d", &arr[j]);
        }
        
        qsort(arr, n, sizeof(int), compare);

        int gap = 0;
        for (int j = 0; j < n - 1; j++){
            if (arr[j + 1] - arr[j] > gap) gap = arr[j + 1] - arr[j];
        }
        
        printf("Max %d, Min %d, Largest gap %d\n", arr[n - 1], arr[0], gap);
    }
    return 0;
}