#include <stdio.h>

int main() {
    int v;
    int a = 0;
    scanf("%d", &v);
    char result[v];
    for (int i =0; i <=v; i++){
        scanf("%c", &result[i]);
        if (result[i] == 'A') a++;
    }
    if (a > v - a) printf("A");
    else if (a < v - a) printf("B");
    else printf("Tie");
    return 0;
}