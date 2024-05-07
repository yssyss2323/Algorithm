#include <stdio.h>

int main()
{
    double A, B;
    double answer;
    scanf("%lf %lf", &A, &B);
    
    answer = A / B;
    
    printf("%.9lf", answer);

    return 0;
}
