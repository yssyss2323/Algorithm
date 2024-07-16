import sys
input = sys.stdin.readline

code_dic = {'0':(1,0),'1':(1,1),'2':(0,1),'3':(-1,1),'4':(-1,0),'5':(-1,-1),'6':(0,-1),'7':(1,-1)}

while True:
    try:
        chain_code = input().strip()
        if not chain_code:
            break
        curr_point = (0,0)
        points = [curr_point]
        a1, a2 = 0, 0
        for code in chain_code:
            next_point = (curr_point[0] + code_dic[code][0], curr_point[1] + code_dic[code][1])
            a1 += curr_point[0] * next_point[1]
            a2 += curr_point[1] * next_point[0]
            curr_point = next_point
            points.append(curr_point)
        s = abs(a1 -a2) / 2
        y = len(chain_code)
        print(int(s + 1 + y / 2))
    except:
        break