#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int box[n];
    for (int x = 0; x < n; x++){
        box[x] = x + 1;
    }
    for (int x = 0; x < m; x++){
        int i, j;
        scanf("%d %d", &i, &j);
        for (int y = i; y <= (i+j)/2; y++){
            int tmp;
            tmp = box[y-1];
            box[y-1] = box[i-1+j-y];
            box[i-1+j-y] = tmp;
        }
    }
    for (int x = 0; x < n; x++){
        printf("%d ", box[x]);
    }
    return 0;
}