#include <stdio.h>

int main() {
    int m;
    scanf("%d", &m);

    int ball[3] = {1, 0, 0};
    for (int i; i < m; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        int tmp = ball[a - 1];
        ball[a - 1] = ball[b - 1];
        ball[b - 1] = tmp;
    }
    for (int i; i < 3; i++){
        if (ball[i] == 1){
            printf("%d", i + 1);
            break;
        }
    }
    return 0;
}