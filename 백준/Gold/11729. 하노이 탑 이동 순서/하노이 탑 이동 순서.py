# 높이 x인 하노이탑 이동순서를 구하는 함수
def f(x):
    if x == 1:
        return '13'
    else:
        tmp1, tmp2 = '', ''
        for i in f(x - 1):
            if i == '1':
                tmp1 += '1'
                tmp2 += '2'
            elif i == '2':
                tmp1 += '3'
                tmp2 += '1'
            else:  # i == 3
                tmp1 += '2'
                tmp2 += '3'
        return tmp1 + '13' + tmp2

n = int(input())
move_num = 2 ** n - 1
move_order = f(n)
print(move_num)
for i in range(move_num):
    print(move_order[i * 2] + ' ' + move_order[i * 2 + 1])