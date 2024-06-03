def find_func(point1, point2):
    a = point1[1] - point2[1]
    b = point2[0] - point1[0]
    c = point1[1] * (point1[0] - point2[0]) - point1[0] * (point1[1] - point2[1])
    return a, b, c

def func_val(a, b, c, point):
    return a * point[0] + b * point[1] + c

def find_intersection(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - b1 * a2
    if det:
        x = (- b2 * c1 + b1 * c2) / det
        y = (a2 * c1 - a1 * c2) / det
        return x, y

def range_check(line1, line2):
    rev_line1 = [[line1[0][1], line1[0][0]], [line1[1][1], line1[1][0]]]
    rev_line2 = [[line2[0][1], line2[0][0]], [line2[1][1], line2[1][0]]]
    line1.sort()
    line2.sort()
    rev_line1.sort()
    rev_line2.sort()
    if line1[0][0] > line2[1][0] or line1[1][0] < line2[0][0] or rev_line1[0][0] > rev_line2[1][0] or rev_line1[1][0] < \
            rev_line2[0][0]:
        return True
    else:
        return False


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    line1 = [[x1, y1], [x2, y2]]
    line2 = [[x3, y3], [x4, y4]]

    if range_check(line1, line2):
        print(0)
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
            print(0)
        elif (start_val1 - start_val2) * (end_val1 - end_val2) == 0:
            print(1)
            if point_start == point_end:
                print(*point_start)
            elif start_val1 - start_val2:
                print(*point_end)
            elif end_val1 - end_val2:
                print(*point_start)
        else:
            print(1)
            print(*find_intersection(a1, b1, c1, a2, b2, c2))
