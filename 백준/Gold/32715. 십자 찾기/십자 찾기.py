import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

board = [[0] * (m + 1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

prefix_sum_row = [[0] * (m + 1) for _ in range(n + 1)]
prefix_sum_col = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum_row[i][j] = prefix_sum_row[i][j - 1] + board[i][j]
        prefix_sum_col[i][j] = prefix_sum_col[i - 1][j] + board[i][j]

ans = 0
target_len = 2 * k + 1

for i in range(k + 1, n + 1 - k):
    for j in range(k + 1, m + 1 - k):
        if prefix_sum_row[i][j + k] - prefix_sum_row[i][j - k - 1] == target_len:
            if prefix_sum_col[i + k][j] - prefix_sum_col[i - k - 1][j] == target_len:
                ans += 1
                    
print(ans)