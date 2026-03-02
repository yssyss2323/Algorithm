for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        a = 10
    if a in (1, 5, 6, 10):
        print(a)
    elif a in (4, 9):
        print(a if b % 2 else a ** 2 % 10)
    else:
        b %= 4
        if b == 0:
            b = 4
        print(a ** b % 10)