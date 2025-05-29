#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int scores[n];
    int min = 1000;
    int max = 0;
    for (int i = 0 ; i < n; i++) {
        scanf("%d", &scores[i]);
        if (min > scores[i]) min = scores[i];
        if (max < scores[i]) max = scores[i];
    }
    printf("%d", max - min);
    return 0;
}