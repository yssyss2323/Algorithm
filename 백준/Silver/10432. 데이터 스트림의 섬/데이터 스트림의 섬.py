import sys
input = sys.stdin.readline

p = int(input())
for x in range(p):
    arr = list(map(int, input().split()))[1:]
    cnt = 0
    for i in range(1, 11):
        if arr[i] > arr[i - 1]:
            curr_min = arr[i]
            for j in range(i, 11):
                if arr[j] < curr_min:
                    curr_min = arr[j]
                if curr_min > max(arr[i - 1], arr[j + 1]):
                    cnt += 1
    print(x + 1, cnt)
