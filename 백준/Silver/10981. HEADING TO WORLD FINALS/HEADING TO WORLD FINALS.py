import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
arr.sort(key=lambda x: (-int(x[2]), int(x[3])))

cnt = 0
check = set()
for i in range(n):
    if arr[i][0] not in check:
        cnt += 1
        check.add(arr[i][0])
        print(arr[i][1])
    if cnt == k:
        break