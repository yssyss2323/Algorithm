#include <stdio.h>
#define MAX_LEN 100

int main() {
    char word[MAX_LEN + 1];
    scanf("%s", word);

    for (int i = 0; i < MAX_LEN + 1; i++){
        if (word[i] == '\0') break;
        if (i > 0 && i % 10 == 0) printf("\n");
        printf("%c", word[i]);
    }
    
    return 0;
}