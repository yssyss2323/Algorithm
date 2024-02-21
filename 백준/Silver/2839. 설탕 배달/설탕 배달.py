n = int(input())
if n in [1, 2, 4, 7]:
    print(-1)
else:
    for i in range(n // 5, -1, -1):
        if (n - 5 * i) % 3 == 0:
            x = (n - 5 * i) // 3
            print(i + x)
            break
