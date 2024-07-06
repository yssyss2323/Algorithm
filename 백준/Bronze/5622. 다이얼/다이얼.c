#include <stdio.h>
#define BUFFER 16

int main() {
    char word[BUFFER];
    scanf("%s", word);
    int i = 0;
    int ans = 0;
    while (word[i] != '\0'){
        int n;
        n = (int) word[i] - 65;
        if (n <= 14) ans += n / 3 + 3;
        else{
            if (n <= 18) ans += 8;
            else if (n <= 21) ans += 9;
            else ans += 10;
        }
        //printf("%d",ans);
        i++;
    }
    printf("%d", ans);
    return 0;
}