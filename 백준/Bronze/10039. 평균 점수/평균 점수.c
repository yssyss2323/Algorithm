#include <stdio.h>

int main() {
    int ans = 0;
    for (int i = 0; i < 5; i++){
        int tmp;
        scanf("%d", &tmp);
        if (tmp < 40) tmp = 40;
        ans += tmp / 5;
    }
    printf("%d", ans);
}