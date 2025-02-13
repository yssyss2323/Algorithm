#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}


int main() {
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++){
        int j = 0, n = 0;
        scanf("%d %d", &j, &n);

        int box[n];
        
        for (int k = 0; k < n; k++){
            int r = 0, c = 0;
            scanf("%d %d", &r, &c);

            box[k] = r * c;
        }

        bubbleSort(box, n);

        int ans = 0;
        for (int k = 0; k < n; k++){
            j -= box[k];
            ans += 1;
            if (j <= 0) break;
        }

        printf("%d\n", ans);   
    }
    return 0;
}