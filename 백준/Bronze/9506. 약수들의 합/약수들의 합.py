def find_factor(x):
    arr = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            arr.add(i)
            arr.add(x // i)
    arr = list(arr)
    arr.sort()
    return arr

while True:
    n = int(input())
    if n == -1:
        break
    tmp = find_factor(n)[:-1]
    if n == sum(tmp):
        ans = ' + '.join(map(str,tmp))
        ans = '= ' + ans
    else:
        ans = 'is NOT perfect.'
    print(f"{n} {ans}")
