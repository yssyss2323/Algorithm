import sys
input = sys.stdin.readline

n = int(input())
check = [list(map(int, input().split())) for _ in range(n)]
check.sort()

arr = [check[0]]
for i in range(1, n):
    curr = check[i]
    stand = arr[-1]
    if stand[1] < curr[0]:
        arr.append(curr)
    else:
        if stand[1] < curr[1]:
            arr[-1][1] = curr[1]
ans = 0
for point in arr:
    ans += point[1] - point[0]
print(ans)