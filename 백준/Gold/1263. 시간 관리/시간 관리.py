import sys

input = sys.stdin.readline

n = int(input())
time_table = []
for _ in range(n):
    t, s = map(int, input().split())
    time_table.append([s, s - t])
time_table.sort(reverse=True)
for i in range(n - 1):
    time = time_table[i]
    end, start = time
    gap = start - time_table[i + 1][0]
    if gap < 0:
        time_table[i + 1][0] += gap
        time_table[i + 1][1] += gap

ans = time_table[-1][1]
print(ans if ans >= 0 else -1)
