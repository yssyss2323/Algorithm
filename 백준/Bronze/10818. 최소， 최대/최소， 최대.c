#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    
    int num[N];
    int min = 1e6;
    int max = -1e6;
    for (int i = 0; i < N; i++){
        
        scanf("%d", &num[i]);
        if (num[i] < min) min = num[i];
        if (num[i] > max) max = num[i];
    }
    
    printf("%d %d", min, max);

    return 0;
}
