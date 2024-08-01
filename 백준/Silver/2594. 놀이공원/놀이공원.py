n = int(input())
time_table = [list(map(lambda x : int(x[:2]) * 60 + int(x[2:]), input().split())) for _ in range(n)]
time_table.sort()

ans = max(time_table[0][0] - 60 * 10 - 10, 0)
end = 0
for i in range(n - 1):
    start1, end1 = time_table[i]
    start2, end2 = time_table[i + 1]
    end = max(end, end1)
    ans = max(0, ans, start2 - end - 20)
end = max(end, time_table[-1][1])
ans = max(ans,  60 * 22 - end - 10)
print(ans)