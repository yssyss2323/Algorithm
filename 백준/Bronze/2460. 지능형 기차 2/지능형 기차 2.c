#include <stdio.h>

int main() {
    int ans = 0;
    int tmp = 0;

    for (int i = 0; i < 10; i++){
        int out, in;
        scanf("%d %d", &out, &in);
        tmp += in - out;
        if (tmp > ans) ans = tmp;
    }

    printf("%d", ans);
    return 0;
}