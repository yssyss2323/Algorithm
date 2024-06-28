def printstar(n, x, i):
    if i == 1 or i == 4 * x - 3:
        print('*' * (4 * x - 3), end='')
        if n == x: print()
    elif i == 2 or i == 4 * x - 4:
        print('*' + ' ' * (4 * x - 5) + '*', end='')
        if n == x: print()
    else:
        print('* ', end='')
        printstar(n, x - 1, i - 2)
        print(' *', end='')
        if n == x: print()


n = int(input())
for i in range(1, 4 * n - 3 + 1):
    printstar(n, n, i)
