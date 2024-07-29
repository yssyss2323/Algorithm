def print_star(x):
    if x == 1:
        return ['*']
    if x == 2:
        return ['*****', ' ***', '  *']
    if x % 2:
        arr = print_star(x - 1)
        n = len(arr[0])
        star_arr = []
        star_arr.append(' ' * (n + 1) + '*')
        for i in range(1, n + 1):
            tmp = ' ' * (n + 1 - i) + '*'
            if (n + 1) // 2 <= i <= n + 1:
                tmp += ' ' * (i - (n + 1) // 2)
                tmp += arr[i - (n + 1) // 2]
                tmp += ' ' * (2 * (i - (n + 1) // 2)) + '*'
            else:
                tmp += ' ' * (2 * i - 1) + '*'
            star_arr.append(tmp)
        star_arr.append('*' * (2 * n + 3))
        return star_arr
    else:
        arr = print_star(x - 1)
        n = len(arr[-1])
        star_arr = []
        star_arr.append('*' * (2 * n + 3))
        for i in range(1, n + 1):
            tmp = ' ' * i + '*'
            if i <= (n + 1) // 2:
                tmp += ' ' * ((n + 1) // 2 - i)
                tmp += arr[i - 1]
                tmp += ' ' * (n - i * 2 + 1) + '*'
            else:
                tmp += ' ' * (2 * n + 3 - 2 * (i + 1)) + '*'
            star_arr.append(tmp)
        star_arr.append(' ' * (n + 1) + '*')
        return star_arr


n = int(input())
for star in print_star(n):
    print(*star, sep='')
