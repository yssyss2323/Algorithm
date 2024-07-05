#include <stdio.h>

int main() {
    int n,m;
    scanf("%d %d", &n, &m);
    int box[n];
    for (int i = 0; i < n; i++){
        box[i] = i+1;
    }

    for (int x = 0; x < m; x++){
        int i,j;
        scanf("%d %d", &i, &j);
        int tmp = box[i-1];
        box[i-1] = box[j-1];
        box[j-1] = tmp;
    }
    for (int i = 0; i < n; i++){
        printf("%d ", box[i]);
    }
    return 0;
}