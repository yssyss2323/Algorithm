import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
board = [[0] * (m + 1)]
board += [[0] + list(map(int, input().split())) for _ in range(n)]

prefix_sum_row = [[0] * (m + 1)]
for i in range(1, n + 1):
    curr_row = [0]
    tmp = 0
    for j in range(1, m + 1):
        tmp += board[i][j]
        curr_row.append(tmp)
    prefix_sum_row.append(curr_row)

prefix_sum_col = [[0] for _ in range(n + 1)]
prefix_sum_col[0] = [0] * (m + 1)
for i in range(1, m + 1):
    tmp = 0
    for j in range(1, n + 1):
        tmp += board[j][i]
        prefix_sum_col[j].append(tmp)

ans = 0
for i in range(k + 1, n + 1 - k):
    for j in range(k + 1, m + 1 - k):
        if prefix_sum_row[i][j + k] - prefix_sum_row[i][j - k - 1] == 2 * k + 1:
            if prefix_sum_col[i + k][j] - prefix_sum_col[i - k - 1][j] == 2 * k + 1:
                ans += 1
print(ans)