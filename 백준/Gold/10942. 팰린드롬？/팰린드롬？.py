import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
table = [[0] * n for _ in range(n)]
for i in range(n):
    table[i][i] = 1
    for j in range(1, n - i):
        if i - j < 0:
            break
        if nums[i - j] == nums[i + j]:
            table[i - j][i + j] = 1
        else:
            break
for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        table[i][i + 1] = 1
        for j in range(1, n - i - 1):
            if i - j < 0:
                break
            if nums[i - j] == nums[i + 1 + j]:
                table[i - j][i + 1 + j] = 1
            else:
                break

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(table[s - 1][e - 1])
