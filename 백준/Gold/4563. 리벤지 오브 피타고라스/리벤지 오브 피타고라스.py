def counting(x):
    cnt = 0
    for i in range(1, x):
        if x ** 2 % i == 0 and i % 2 == (x ** 2 // i) % 2:
            if ((x ** 2 // i) - i) // 2 > x:
                cnt += 1
            else:
                break
    return cnt


while True:
    A = int(input())
    if A == 0: break

    print(counting(A))
