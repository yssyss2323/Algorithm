#include <stdio.h>
#define MAX 260

int main() {
    char string[MAX];
    gets(string);

    int happy = 0, sad = 0;

    for (int i = 0; i < MAX; i++){
        if (string[i] == ':' && string[i + 1] == '-') {
            if (string[i + 2] == ')') happy += 1;
            else if (string[i + 2] == '(') sad += 1;
        }
    }
    if (happy == 0 && sad == 0) printf("none");
    else if (happy == sad) printf("unsure");
    else if (happy > sad) printf("happy");
    else printf("sad");
    return 0;
}