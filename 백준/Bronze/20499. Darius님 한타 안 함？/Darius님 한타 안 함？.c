#include <stdio.h>
#include <string.h>
#define LEN 10

int main() {
    char kda[LEN];
    scanf("%s", kda);

    int k, d, a;
    int tmp;
    int idx1 = 0, idx2 = 0;
    for (int i = 0; i < strlen(kda); i++) {
        if (kda[i] == '/') {
            if (idx1 == 0) {
                idx1 = i;
                int tmp = 0;
                for (int j = 0; j < idx1; j++){
                    tmp = tmp * 10 + (kda[j] - '0');
                }
                k = tmp;
            }
            else {
                idx2 = i;
                int tmp = 0;
                for (int j = idx1 + 1; j < idx2; j++){
                    tmp = tmp * 10 + (kda[j] - '0');
                }
                d = tmp;
                
                tmp = 0;
                for (int j = idx2 + 1; j < strlen(kda); j++){
                    tmp = tmp * 10 + (kda[j] - '0');
                }
                a = tmp;
                break;
            }
        }
    }
    
    if (d == 0) printf("hasu");
    else if (k + a < d) printf("hasu");
    else printf("gosu");
    return 0;
}