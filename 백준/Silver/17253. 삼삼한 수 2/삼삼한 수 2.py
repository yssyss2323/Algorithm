n = int(input())

if n == 0:
    print("NO")
else:
    while n > 0:
        if n % 3 == 0:
            n //= 3
        elif n % 3 == 1:
            n = (n - 1) // 3
        else:
            print("NO")
            break
    else:
        print("YES")