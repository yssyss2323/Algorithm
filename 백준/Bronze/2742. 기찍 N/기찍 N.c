#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int ans = 1;
    for (int i = n; i > 0; i--){
        printf("%d\n",i);
    }
    return 0;
}