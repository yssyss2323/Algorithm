import sys
input = lambda: sys.stdin.readline().rstrip()

def calc(arr, height):
    few, much = 0, 0
    for i in range(len(arr)):
        if arr[i]:
            tmp = i - height
            if tmp < 0:
                few += -tmp * arr[i]
            elif tmp > 0:
                much += tmp * arr[i] * 2
                
    if B + much // 2 < few:
        return float('inf')
    
    return few + much

N,M,B = map(int,input().split())
height_blocks = [0] * 257
max_height, min_height = -float('inf'), float('inf')
for _ in range(N):
    tmp = list(map(int,input().split()))
    for i in tmp:
        height_blocks[i] += 1
        if i > max_height:
            max_height = i
        if i < min_height:
            min_height = i
            
height_time = [0] * (max_height - min_height + 1)
min_time = float('inf')
min_time_list = []
for i in range(min_height, max_height + 1):
    i_time = calc(height_blocks, i)
    height_time[i - min_height] = i_time
    if min_time > i_time:
        min_time = i_time
        min_time_list = [i]
    elif min_time == i_time:
        min_time_list.append(i)
answer_height = min_time_list[-1]
print(min_time, answer_height)