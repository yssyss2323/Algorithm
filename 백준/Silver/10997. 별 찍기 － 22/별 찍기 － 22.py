def print_star(n):
    if n == 1:
        return ['*']
    elif n == 2:
        return ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']
    else:
        prev = print_star(n - 1)
        length = len(prev[0])
        arr = ['*' * (length + 4), '*', '* ' + prev[0] + '**']
        for i in range(1, len(prev)):
            star = prev[i]
            arr.append('* ' + star + ' ' * (length - len(star)) + ' *')
        arr.append('*' + ' ' * (length + 2) + '*')
        arr.append('*' * (length + 4))
        return arr

n = int(input())
for star in print_star(n):
    print(star)