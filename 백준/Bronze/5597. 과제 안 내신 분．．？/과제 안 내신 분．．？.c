#include <stdio.h>

int main() {
    int students[30];
    for (int i = 0; i < 30; i++){
        int n;
        scanf("%d", &n);
        students[n - 1] = n;
    }
    for (int i = 0; i < 30; i++){
        if (students[i] != i + 1) printf("%d\n", i + 1);
    }
    return 0;
}