#include <stdio.h>
#include <string.h>
#define MAX_LEN 15

int main() {
    int n;
    scanf("%d", &n);

    char young[MAX_LEN + 1];
    char old[MAX_LEN + 1];

    int young_age = 0;
    int old_age = 20110000;
    
    for (int i; i < n; i++){
        char name[MAX_LEN + 1];
        int day, month, year;

        scanf("%s %d %d %d", name, &day, &month, &year);
        int tmp = year * 10000 + month * 100 + day;
        
        if (tmp > young_age) {
            young_age = tmp;
            strcpy(young, name);
        }
        if (tmp < old_age) {
            old_age = tmp;
            strcpy(old, name);
        }
    }
    printf("%s\n", young);
    printf("%s\n", old);
    return 0;
}