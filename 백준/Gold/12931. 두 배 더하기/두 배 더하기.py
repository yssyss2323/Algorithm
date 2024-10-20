n = int(input())
arr = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        if arr[i] % 2:
            arr[i] -= 1
            ans += 1
    if sum(arr) == 0:
        break
    arr = [x // 2 for x in arr]
    ans += 1
print(ans)