import sys
input = lambda:sys.stdin.readline().rstrip()

b, n, m = map(int, input().split())
check = dict()
for _ in range(n):
    i, p = input().split()
    check[i] = int(p)
ans = 0
for _ in range(m):
    ans += check[input()]
print("acceptable" if b >= ans else "unacceptable")