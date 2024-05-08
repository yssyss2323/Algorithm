CCW, CW, LINE = 1, -1, 0

def point_to_line(x1,y1,x2,y2):
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return a, b, c
    
def find_direction(x1,y1,x2,y2,x3,y3):
    a,b,c = point_to_line(x1,y1,x2,y2)
    if b != 0:
        tmp = -a * x3 - c
        if b * y3 > tmp:
            direction = CCW
        elif b * y3 == tmp:
            direction = LINE
        else:
            direction = CW
    else:
        sign_a = a // abs(a)
        if x3 == x2:
            direction = LINE
        else:
            direction = CW * sign_a if x3 < x2 else CCW * sign_a
    return direction

ax, ay = map(int,input().split())
bx, by = map(int,input().split())
cx, cy = map(int,input().split())

print(find_direction(ax,ay,bx,by,cx,cy))
