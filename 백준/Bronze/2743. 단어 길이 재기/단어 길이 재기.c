#include <stdio.h>
#define BUFFER 101

int main() {
    char words[BUFFER];
    scanf("%s", words);
    int i = 0;
    while (words[i] != '\0'){
        i++;
    }
    printf("%d", i);
    return 0;
}