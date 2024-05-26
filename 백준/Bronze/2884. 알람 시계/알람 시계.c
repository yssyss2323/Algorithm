#include <stdio.h>

int main()
{
    int hour, min;
    scanf("%d %d", &hour, &min);
    
    if (min >= 45) printf("%d %d", hour, min -45);
    else if (hour >= 1) printf("%d %d", hour - 1, min + 15);
    else printf("23 %d", min + 15);

    return 0;
}
