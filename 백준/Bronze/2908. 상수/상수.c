#include <stdio.h>
#define BUFFER 1001

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int reva, revb;
    reva = (a % 10) * 100 + ((a / 10) % 10) * 10 + a / 100;
    revb = (b % 10) * 100 + ((b / 10) % 10) * 10 + b / 100;
    if (a % 10 > b % 10) printf("%d" , reva);
    else if ( a % 10 < b % 10) printf("%d", revb);
    else{
        if ((a / 10) % 10 > (b / 10) % 10) printf("%d" , reva);
        else if ((a / 10) % 10 < (b / 10) % 10) printf("%d", revb);
        else{
            if (a / 100 > b / 100) printf("%d" , reva);
            else printf("%d", revb);
        }
    }
    return 0;
}