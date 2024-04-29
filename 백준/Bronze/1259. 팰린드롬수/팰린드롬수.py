while True:
    tmp = input()
    if tmp == '0':
        break
    for i in range(len(tmp) // 2):
        if tmp[i] != tmp[len(tmp) - i - 1]:
            print('no')
            break
    else:
        print('yes')
