import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numlist = [0] * 10001
for _ in range(N):
    tmp = int(input())
    numlist[tmp] += 1
for i in range(1,10001):
    for _ in range(numlist[i]):
        print(i)