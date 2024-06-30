n = int(input())
for _ in range(n):
    time_table = []
    while True:
        s, f = map(int, input().split())
        if s == 0 and f == 0:
            break
        time_table.append([f, s])
    time_table.sort()

    ans = 1
    start = time_table[0]
    for i in range(1, len(time_table)):
        if time_table[i][1] >= start[0]:
            ans += 1
            start = time_table[i]
    print(ans)
