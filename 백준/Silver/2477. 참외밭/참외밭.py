direction_dic = {1:(1,0),2:(-1,0),3:(0,-1),4:(0,1)}

k = int(input())
curr = (0,0)
points = [curr]
for _ in range(6):
    direction, distance = map(int, input().split())
    curr = (curr[0] + direction_dic[direction][0] * distance, curr[1] + direction_dic[direction][1] * distance)
    points.append(curr)

tmp1, tmp2 = 0, 0
for i in range(6):
    tmp1 += points[i][0] * points[i+1][1]
    tmp2 += points[i][1] * points[i+1][0]
area = abs(tmp1 - tmp2) // 2
print(area * k)