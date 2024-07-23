def check_coin(arr):
    cnt = 0
    for row in arr:
        cnt += sum(row)
    # print(arr, cnt)
    if cnt in (0, 9):
        return True
    return False

def flip(val):
    return (val + 1) % 2

def binary(num):
    tmp = bin(num)[2:]
    case = '0' * (8 - len(tmp)) + tmp
    return case

case_dic = {0:[(0,0), (0,1), (0,2)],
            1:[(1,0), (1,1), (1,2)],
            2:[(2,0), (2,1), (2,2)],
            3:[(0,0), (1,0), (2,0)],
            4:[(0,1), (1,1), (2,1)],
            5:[(0,2), (1,2), (2,2)],
            6:[(0,0), (1,1), (2,2)],
            7:[(0,2), (1,1), (2,0)]}
def flip_line(arr, num):
    tmp_arr = [[val for val in row] for row in arr]
    case = binary(num)
    #print(case)
    for i in range(8):
        if case[i] == '1':
            for coord in case_dic[i]:
                x, y = coord
                tmp_arr[x][y] = flip(tmp_arr[x][y])
    return tmp_arr

t = int(input())
for _ in range(t):
    coins = [[1 if i == 'H' else 0 for i in input().split()] for _ in range(3)]
    ans = float('inf')
    for i in range(256):
        if check_coin(flip_line(coins, i)):
            ans = min(ans, binary(i).count('1'))
            #print('check')
    if ans > 8:
        ans = -1
    print(ans)