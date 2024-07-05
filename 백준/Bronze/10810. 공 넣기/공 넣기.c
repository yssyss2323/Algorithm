#include <stdio.h>
#include <string.h>


int main() {
    int n,m;
    scanf("%d %d", &n, &m);
    int box[n];
    memset(box, 0, sizeof(box));
    for (int x = 0; x < m; x++){
        int i,j,k;
        scanf("%d %d %d", &i, &j, &k);
        for (int y = i; y <= j; y++){
            box[y - 1] = k;
        }
    }
    for (int i = 0; i < n; i++){
        printf("%d ", box[i]);
    }
    return 0;
}