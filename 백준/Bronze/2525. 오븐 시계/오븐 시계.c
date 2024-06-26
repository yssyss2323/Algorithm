#include <stdio.h>

int main() {
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    int h, m;
    int tmp1 = c / 60;
    int tmp2 = c % 60;
    if (b + tmp2 >= 60){
        m = b + tmp2 - 60;
        if (a + tmp1 + 1 >= 24) h = a + tmp1 + 1 -24;
        else h = a + tmp1 + 1;
    }
    else {
        m = b + tmp2;
        if (a + tmp1 >= 24) h = a + tmp1 -24;
        else h = a + tmp1;
    }
    printf("%d %d",h,m);
    return 0;
}