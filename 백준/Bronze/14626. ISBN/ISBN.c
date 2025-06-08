#include <stdio.h>
#define LEN 13

int main() {
    char isbn[LEN];
    gets(isbn);

    int tot = 0;
    int mod_inv = 1;
    for (int i = 0; i < LEN; i++) {
        if (isbn[i] == '*') {
            if (i % 2 == 1) mod_inv = 7;
        }
        else {
            int curr = isbn[i] - '0';
            if (i % 2 == 1) curr *= 3;
            tot += curr;  
        }
    }
    int ans = 10 - (tot * mod_inv) % 10;
    if (ans == 10) ans = 0;
    printf("%d", ans);
    return 0;
}