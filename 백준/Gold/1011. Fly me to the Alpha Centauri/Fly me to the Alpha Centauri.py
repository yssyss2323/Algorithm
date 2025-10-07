def solv(dist):
    if dist <= 3:
        print(dist)
    else:
        n = int(dist ** 0.5)
        if n == dist ** 0.5:
            print(2 * n - 1)
        elif dist <= n * (n + 1):
            print(2 * n)
        else:
            print(2 * n + 1)


for _ in range(int(input())):
    x, y = map(int, input().split())
    solv(y - x)