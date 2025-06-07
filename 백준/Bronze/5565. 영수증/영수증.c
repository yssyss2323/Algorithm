#include <stdio.h>

int main() {
    int tot;
    scanf("%d", &tot);
    for (int i = 0; i < 9; i++) {
        int tmp;
        scanf("%d", &tmp);
        tot -= tmp;
    }

    printf("%d", tot);
    return 0;
}