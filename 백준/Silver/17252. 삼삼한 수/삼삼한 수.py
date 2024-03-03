n = int(input())
if n == 0:
    print("NO")
else:
    while n > 3:
        if n % 3 == 2:
            print('NO')
            break
        else:
            n //= 3
    else:
        if n == 2:
            print('NO')
        else:
            print('YES')