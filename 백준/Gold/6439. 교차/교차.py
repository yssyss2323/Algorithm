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
            return False
        elif (start_val1 - start_val2) * (end_val1 - end_val2) == 0:
            if point_start == point_end:
                return True
            elif start_val1 - start_val2 or end_val1 - end_val2:
                if b1 == 0:
                    if line2[1][0] == line1[0][0] and line2[1][1] < line1[0][1]:
                        return False
                    if line2[0][0] == line1[0][0] and line2[0][1] > line1[1][1]:
                        return False
                elif b2 == 0:
                    if line1[1][0] == line2[0][0] and line1[1][1] < line2[0][1]:
                        return False
                    if line1[0][0] == line2[0][0] and line1[0][1] > line2[1][1]:
                        return False
                return True
            else:
                return True
        else:
            return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        square = []
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        line = [[x1, y1], [x2, y2]]
        if (min(line[0][0], line[1][0]) >= min(x3, x4) and max(line[0][0], line[1][0]) <= max(x3, x4) and
                min(line[0][1], line[1][1]) >= min(y3, y4) and max(line[0][1], line[1][1]) <= max(y3, y4)):
            print('T')
        else:
            square.append([[x3, y3], [x3, y4]])
            square.append([[x3, y3], [x4, y3]])
            square.append([[x4, y4], [x3, y4]])
            square.append([[x4, y4], [x4, y3]])
            for i in range(4):
                if relation(line, square[i]):
                    print('T')
                    break
            else:
                print('F')
