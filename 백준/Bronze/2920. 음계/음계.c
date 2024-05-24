#include <stdio.h>

int main()
{
    int nums[8];
    int key1 = 0, key2 = 0;
    
    for (int i; i < 8; i++){
        scanf("%d", &nums[i]);
        if (nums[i] != i + 1) key1 = -1;
        if (nums[i] != 8 - i) key2 = -1;
    }
    
    if (key1 == 0) printf("ascending");
    else if (key2 == 0) printf("descending");
    else printf("mixed");

    return 0;
}
