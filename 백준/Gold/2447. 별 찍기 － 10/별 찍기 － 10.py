def print_star(n):
    if n == 3:
        return ['***', '* *', '***']
    stars = []
    for star in print_star(n // 3):
        stars.append(star * 3)
    for star in print_star(n // 3):
        stars.append(star + ' ' * (n // 3) + star)
    for star in print_star(n // 3):
        stars.append(star * 3)
    return stars


n = int(input())
for star in print_star(n):
    print(star)
