def get_Kantor(x):
    if x == 0:
        print('-', end='')
    else:
        get_Kantor(x - 1)
        print(' ' * 3 ** (x - 1), end='')
        get_Kantor(x - 1)


while True:
    try:
        n = int(input())
        get_Kantor(n)
        print()
    except:
        break
