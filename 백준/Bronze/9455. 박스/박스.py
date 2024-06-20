def cal_col(arr, l):
    sum = 0
    cnt = 0
    x = len(arr)
    for i in range(x):
        if arr[i] == 1:
            cnt += 1
            sum += l - 1 - i
    return sum - (cnt - 1) * cnt // 2

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    columns = [[] for _ in range(n)]
    for _ in range(m):
        tmp = list(map(int, input().split()))
        for i in range(n):
            columns[i].append(tmp[i])

    ans = 0
    for col in columns:
        ans += cal_col(col, m)
    print(ans)
