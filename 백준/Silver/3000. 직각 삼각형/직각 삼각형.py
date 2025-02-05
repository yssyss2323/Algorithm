import sys
input = sys.stdin.readline

n = int(input())
x_dic, y_dic = {}, {}
points = []
for _ in range(n):
    x, y = map(int, input().split())
    x_dic[x] = x_dic.get(x, 0) + 1
    y_dic[y] = y_dic.get(y, 0) + 1
    points.append((x, y))

ans = 0
for x, y in points:
    ans += (x_dic[x] - 1) * (y_dic[y] - 1)
print(ans)