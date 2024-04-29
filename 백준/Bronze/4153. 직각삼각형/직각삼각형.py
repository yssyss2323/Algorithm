while True:
    tmp = list(map(int, input().split()))
    if tmp == [0, 0, 0]:
        break
    tmp.sort()
    if tmp[0] ** 2 + tmp[1] ** 2 == tmp[2] ** 2:
        print('right')
    else:
        print('wrong')
