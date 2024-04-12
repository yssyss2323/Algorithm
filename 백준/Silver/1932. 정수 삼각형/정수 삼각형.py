import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
triangle = []
for _ in range(n):
    triangle = [list(map(int, input().split()))] + triangle
for i in range(1, n):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j + 1])
print(triangle[-1][-1])
