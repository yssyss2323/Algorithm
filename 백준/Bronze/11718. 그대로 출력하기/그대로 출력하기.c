#include <stdio.h>
#define BUFFER 101

int main() {
    while (1){
        char word[BUFFER];
        if (fgets(word, sizeof(word),stdin) == NULL) break;
        
        printf("%s", word);
    }
    return 0;
}