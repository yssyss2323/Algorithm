for _ in range(int(input())):
    _ = input()
    tmp = input()
    if '!' in tmp:
        print('!')
    else:
        tot = sum(map(int, tmp.split(' + ')))
        if tot > 9:
            print('!')
        else:
            print(tot)