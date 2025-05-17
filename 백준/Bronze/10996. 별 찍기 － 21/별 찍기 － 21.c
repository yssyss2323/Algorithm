#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n == 1) printf("*");
    else {
        for (int x = 0; x < n; x++) {
            for (int j = 0; j < 2; j++) {
                for (int i = 0; i < n; i++) {
                    if ((i + j) % 2 == 0) printf("*");
                    else printf(" ");
                }
            printf("\n");
            }
        }
    }
}