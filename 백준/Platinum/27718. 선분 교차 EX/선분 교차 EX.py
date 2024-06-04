def find_func(point1, point2):
    a = point1[1] - point2[1]
    b = point2[0] - point1[0]
    c = - point1[1] * b - point1[0] * a
    return a, b, c

def func_val(a, b, c, point):
    return a * point[0] + b * point[1] + c

def range_check(line1, line2):
    rev_line1 = [[line1[0][1], line1[0][0]], [line1[1][1], line1[1][0]]]
    rev_line2 = [[line2[0][1], line2[0][0]], [line2[1][1], line2[1][0]]]
    line1.sort()
    line2.sort()
    rev_line1.sort()
    rev_line2.sort()
    if (line1[0][0] > line2[1][0] or line1[1][0] < line2[0][0] or
            rev_line1[0][0] > rev_line2[1][0] or rev_line1[1][0] < rev_line2[0][0]):
        return True
    else:
        return False

def relation(line1, line2):
    if range_check(line1, line2):
        return 0
    else:
        a1, b1, c1 = find_func(line1[0], line1[1])
        a2, b2, c2 = find_func(line2[0], line2[1])

        point_start = max(line1[0], line2[0])
        point_end = min(line1[1], line2[1])

        start_val1 = func_val(a1, b1, c1, point_start)
        start_val2 = func_val(a2, b2, c2, point_start)
        end_val1 = func_val(a1, b1, c1, point_end)
        end_val2 = func_val(a2, b2, c2, point_end)

        if (start_val1 - start_val2) * (end_val1 - end_val2) > 0:
            return 0
        elif (start_val1 - start_val2) * (end_val1 - end_val2) == 0:
            if point_start == point_end:
                return 1
            elif start_val1 - start_val2 or end_val1 - end_val2:
                if b1 == 0:
                    if line2[1][0] == line1[0][0] and line2[1][1] < line1[0][1]:
                        return 0
                    if line2[0][0] == line1[0][0] and line2[0][1] > line1[1][1]:
                        return 0
                elif b2 == 0:
                    if line1[1][0] == line2[0][0] and line1[1][1] < line2[0][1]:
                        return 0
                    if line1[0][0] == line2[0][0] and line1[0][1] > line2[1][1]:
                        return 0
                return 1
            else:
                return 3
        else:
            return 2


if __name__ == "__main__":
    import sys
    input = lambda: sys.stdin.readline().rstrip()

    N = int(input())
    lines = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        tmp_line = [[x1, y1], [x2, y2]]
        lines.append(tmp_line)

    answer = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j > i:
                answer[i][j] = relation(lines[i], lines[j])
            elif j == i:
                answer[i][j] = 3
            else:
                answer[i][j] = answer[j][i]
        print(*answer[i], sep='')
