def solv(arr):
    ans = -float('inf')
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] - arr[j] > ans:
                ans = arr[i] - arr[j]
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    suffix_sum = [0]
    tmp = 0
    for i in range(n):
        tmp += arr[i]
        suffix_sum.append(tmp)
    print(solv(suffix_sum))