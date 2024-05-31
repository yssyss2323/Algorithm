def find_func(point1,point2):
    a = point1[1] - point2[1]
    b = point2[0] - point1[0]
    c = point1[1] * (point1[0] - point2[0]) - point1[0] * (point1[1] - point2[1])
    return a,b,c

def func_val(a,b,c,point):
    return a * point[0] + b * point[1] + c


if __name__ == "__main__":
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = map(int,input().split())
    line1 = [[x1,y1],[x2,y2]]
    line1.sort()
    line2 = [[x3,y3],[x4,y4]]
    line2.sort()

    if line1[0][0] > line2[1][0] or line1[1][0] < line2[0][0]:
        print(0)
    else:
        a1,b1,c1 = find_func(line1[0],line1[1])
        a2,b2,c2 = find_func(line2[0],line2[1])

        point_start = max(line1[0], line2[0])
        point_end = min(line1[1],line2[1])

        start_val1 = func_val(a1,b1,c1,point_start)
        start_val2 = func_val(a2,b2,c2,point_start)
        end_val1 = func_val(a1,b1,c1,point_end)
        end_val2 = func_val(a2,b2,c2,point_end)

        if (start_val1 - start_val2) * (end_val1 - end_val2) <= 0:
            print(1)
        else:
            print(0)
