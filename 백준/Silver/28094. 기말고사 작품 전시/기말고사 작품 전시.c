#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void permute(int *arr, int l, int r, int **results, int *index) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            results[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap((arr + l), (arr + i));
            permute(arr, l + 1, r, results, index);
            swap((arr + l), (arr + i)); // backtrack
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);

        int ab[n + 1][n + 1];
        memset(ab, 0, sizeof(ab));

        for (int i = 0; i < m; i++) {
            int v, a, b;
            scanf("%d %d %d", &v, &a, &b);
            ab[a][b] += v;
        }

        // 순열 생성
        int *arr = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        // 최대 순열 개수: n!
        int max_permutations = 1;
        for (int i = 2; i <= n; i++) {
            max_permutations *= i;
        }

        int **cases = (int **)malloc(max_permutations * sizeof(int *));
        for (int i = 0; i < max_permutations; i++) {
            cases[i] = (int *)malloc(n * sizeof(int));
        }

        int index = 0;
        permute(arr, 0, n - 1, cases, &index);

        int maximum = -1;
        int cnt = 0;

        for (int i = 0; i < max_permutations; i++) {
            int score = 0;
            for (int j = 0; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    score += ab[cases[i][j]][cases[i][k]];
                }
            }
            if (score > maximum) {
                maximum = score;
                cnt = 1;
            } else if (score == maximum) {
                cnt++;
            }
        }

        printf("%d %d\n", maximum, cnt);

        // 메모리 해제
        for (int i = 0; i < max_permutations; i++) {
            free(cases[i]);
        }
        free(cases);
        free(arr);
    }

    return 0;
}