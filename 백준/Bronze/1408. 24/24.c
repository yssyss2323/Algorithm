#include <stdio.h>


int main() {
    char curr[8];
    char start[8];
    scanf("%s %s", curr, start);

    int dh = (start[0] - curr[0]) * 10 + (start[1] - curr[1]);
    int dm = (start[3] - curr[3]) * 10 + (start[4] - curr[4]);
    int ds = (start[6] - curr[6]) * 10 + (start[7] - curr[7]);

    if (ds < 0) {
        ds += 60;
        dm -= 1;
    }

    if (dm < 0) {
        dm += 60;
        dh -= 1;
    }

    if (dh < 0) {
        dh += 24;
        
    }

    printf("%02d:%02d:%02d", dh, dm, ds);
    return 0;
}