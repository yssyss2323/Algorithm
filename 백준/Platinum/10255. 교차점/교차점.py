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
    rev_line1.sort()
    #rev_line2.sort()
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
                return float('inf')
        else:
            return 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        square = []
        x1, y1, x2, y2 = map(int, input().split())
        points = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
        square.append([points[0], points[1]])
        square.append([points[0], points[2]])
        square.append([points[1], points[3]])
        square.append([points[2], points[3]])
        p, q, r, s = map(int, input().split())
        line = [[p, q], [r, s]]
        line.sort()

        cnt = 0
        for i in range(4):
            cnt += relation(line, square[i])

        a, b, c = find_func(line[0], line[1])
        for point in points:
            if (line[0][0] <= point[0] <= line[1][0]
                    and min(line[0][1], line[1][1]) <= point[1] <= max(line[0][1], line[1][1])):
                if func_val(a, b, c, point) == 0:
                    cnt -= 1

        if cnt == float('inf'):
            print(4)
        else:
            print(cnt)
