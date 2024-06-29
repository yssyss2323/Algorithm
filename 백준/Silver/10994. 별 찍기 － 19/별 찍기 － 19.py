def print_star(x):
    if x == 1:
        return ['*']

    stars = []
    stars.append('*' * (4 * x - 3))
    stars.append('*' + ' ' * (4 * x - 5) + '*')
    for star in print_star(x-1):
        stars.append('* ' + star + ' *')
    stars.append('*' + ' ' * (4 * x - 5) + '*')
    stars.append('*' * (4 * x - 3))
    return stars


n = int(input())
for star in print_star(n):
    print(star)
