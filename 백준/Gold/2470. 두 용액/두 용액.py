n = int(input())
arr = list(map(int, input().split()))
arr.sort()

s, e = 0, n - 1
val = float('inf')
ans = [arr[s], arr[e]]
while s < e:
    if abs(arr[s] + arr[e]) < val:
        val = abs(arr[s] + arr[e])
        ans = [arr[s], arr[e]]
    if abs(arr[s]) < abs(arr[e]):
        e -= 1
    else:
        s += 1
print(*ans)