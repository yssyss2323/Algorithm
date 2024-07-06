#include <stdio.h>
#define BUFFER 1001

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++){
        char words[BUFFER];
        scanf("%s", words);
        int j = 0;
        while (words[j] != '\0'){
            j++;
        }
        printf("%c%c\n",words[0], words[--j]);
    }
    return 0;
}