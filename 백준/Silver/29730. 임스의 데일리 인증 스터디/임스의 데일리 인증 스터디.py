import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
bj = []
arr = []
for _ in range(n):
    curr = input()
    if "boj.kr/" in curr:
        bj.append((len(curr), curr))
    else:
        arr.append((len(curr), curr))
arr.sort()
bj.sort()
arr += bj
for i in range(n):
    print(arr[i][1])