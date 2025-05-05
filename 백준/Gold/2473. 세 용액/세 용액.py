n = int(input())
arr = list(map(int, input().split()))
arr.sort()

val = float('inf')
ans = []

for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        if val > abs(arr[i] + arr[l] + arr[r]):
            val = abs(arr[i] + arr[l] + arr[r])
            ans = [arr[i], arr[l], arr[r]]

        if arr[i] + arr[l] + arr[r] > 0:
            r -= 1
        elif arr[i] + arr[l] + arr[r] < 0:
            l += 1
        else:
            break

print(*ans)