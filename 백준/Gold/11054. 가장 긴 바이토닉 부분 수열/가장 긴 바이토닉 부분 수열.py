n = int(input())
arr1 = list(map(int, input().split()))
arr2 = arr1[::-1]

dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr1[i] > arr1[j]:
            if dp1[i] < dp1[j] + 1:
                dp1[i] = dp1[j] + 1
        if arr2[i] > arr2[j]:
            if dp2[i] < dp2[j] + 1:
                dp2[i] = dp2[j] + 1

print(max([dp1[i] + dp2[n - 1 - i] - 1 for i in range(n)]))