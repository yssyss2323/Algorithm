n = int(input())
arr = list(map(int, input().split()))
if n % 2:
    arr.append(0)
    n += 1
arr.sort()
ans = 0
for i in range(n // 2):
    tmp = arr[i] + arr[n - i - 1]
    if tmp > ans:
        ans = tmp
print(ans)