import sys
input = sys.stdin.readline

n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
suffix_sum = [[0] * (n + 1)]
for row in farm:
    tmp = 0
    tmp_row = [0]
    for i in range(n):
        tmp += row[i]
        tmp_row.append(tmp + suffix_sum[-1][i + 1])
    suffix_sum.append(tmp_row)

ans = -float('inf')
for i in range(n):
    for j in range(n):
        for k in range(1, n + 1):
            if i + k > n or j + k > n: continue
            tmp = suffix_sum[i + k][j + k] - suffix_sum[i + k][j] - suffix_sum[i][j + k] + suffix_sum[i][j]
            if tmp > ans:
                ans = tmp
print(ans)
