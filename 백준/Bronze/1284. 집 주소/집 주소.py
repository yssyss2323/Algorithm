while True:
    n = input()
    if n == '0':
        break

    zero = n.count('0')
    one = n.count('1')
    etc = len(n) - zero - one
    ans = len(n) + 1 + 4 * zero + 2 * one + 3 * etc
    print(ans)