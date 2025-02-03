def get_area(point1, point2, point3):
    return abs((point1[0] * point2[1] + point2[0] * point3[1] + point3[0] * point1[1])
            - (point1[1] * point2[0] + point2[1] * point3[0] + point3[1] * point1[0])) / 2

n = int(input())
ans = 0
points = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp_area = get_area(points[i], points[j], points[k])
            if tmp_area > ans:
                ans = tmp_area
print(ans)