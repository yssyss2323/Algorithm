def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)

def point_on_edge(x,y):
    if x == 0:
        return abs(y)
    elif y == 0:
        return abs(x)
    else:
        return gcd(abs(x),abs(y))

t = int(input())
for tt in range(t):
    m = int(input())
    curr_point = (0,0)
    points = [curr_point]
    E = 0
    for _ in range(m):
        dx, dy = map(int, input().split())
        E += point_on_edge(dx, dy)
        next_point = (curr_point[0] + dx, curr_point[1] + dy)
        curr_point = next_point
        points.append(curr_point)
    a1, a2 = 0, 0
    for i in range(m):
        a1 += points[i][0] * points[i+1][1]
        a2 += points[i][1] * points[i+1][0]
    A = abs(a1 - a2) / 2
    I = int(A + 1 - E / 2)
    print(f"Scenario #{tt+1}:")
    print(f"{I} {E} {A:.1f}\n")