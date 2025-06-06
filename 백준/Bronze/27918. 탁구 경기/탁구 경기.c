#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int d = 0, p = 0;
    for (int i = 0; i < n; i++) {
        char tmp;
        scanf(" %c", &tmp);
        if (tmp == 'D') d++;
        else p++;

        if (d - p == 2 || p - d == 2) break;
    }

    printf("%d:%d", d, p);
    
    return 0;
}