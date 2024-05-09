#include <stdio.h>

int main()
{
    int length[3];
    scanf("%d %d %d", &length[0], &length[1], &length[2]);
    
    int total_length = length[0] + length[1] + length[2];
    
    int max = 0;
    for (int i = 0; i < 3; i++){
        if (length[i] > max) max = length[i];
    }
    
    while (max * 2 >= total_length){
        max--;
        total_length--;
    }
    printf("%d", total_length);

    return 0;
}
