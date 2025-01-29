#include <stdio.h>

int main() {
    int day;
    int num[5];
    int ans = 0;

    scanf("%d", &day);
    for (int i = 0; i < 5; i++){
        scanf("%d", &num[i]);
        if (num[i] == day) ans += 1;
    }

    printf("%d", ans);
    return 0;
}