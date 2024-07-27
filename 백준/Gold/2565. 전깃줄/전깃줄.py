num_line = int(input())
tmp_lines = [tuple(map(int, input().split())) for _ in range(num_line)]
tmp_lines.sort()
lines = [tmp_lines[i][1] for i in range(num_line)]

dp = [0] * num_line
dp[0] = 1
curr = lines[0]
for i in range(1, num_line):
    tmp = 1
    for j in range(i):
        if lines[i] > lines[j]:
            tmp = max(tmp, dp[j] + 1)
    dp[i] = tmp
ans = num_line - max(dp)
print(ans)