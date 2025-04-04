def rooting(num):
    i = 2
    cnt = 0
    while i ** 2 <= num:
        if num % i == 0:
            cnt += 1
            while num % i == 0:
                num //= i
        else:
            i += 1
    if num > 1:
        cnt += 1
    return cnt


for _ in range(int(input())):
    n = int(input())
    cnt = rooting(n)
    if cnt == 0:
        print(1)
    else:
        print(2 ** (cnt - 1))