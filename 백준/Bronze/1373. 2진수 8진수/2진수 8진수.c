#include <stdio.h>
#include <string.h>
#define LEN 1000001

int main() {
    char num[LEN];
    scanf("%s", num);
    
    int len = strlen(num);
    int pad = (3 - len % 3) % 3;

    char padded[LEN + 3] = {0};
    for (int i = 0; i < pad; i++) {
        padded[i] = '0';
    }
    strcpy(padded + pad, num);
    len += pad;

    for (int i = 0; i < len; i += 3) {
        int d = (padded[i] - '0') * 4 + (padded[i + 1] - '0') * 2 + (padded[i + 2] - '0');
        printf("%d", d);
    }

    return 0;
}