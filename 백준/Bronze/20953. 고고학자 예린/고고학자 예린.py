import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    sum = (a + b) * (a + b) * (a + b - 1) // 2
    print(sum)