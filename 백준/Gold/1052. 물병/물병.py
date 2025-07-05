n, k = map(int, input().split())

check = bin(n)[2:]
if check.count('1') <= k:
    print(0)
else:
    cnt = 0
    for i in range(len(check)):
        if check[i] == '1':
            cnt += 1
        if cnt == k:
            tmp1 = '0b1' + '0' * (len(check) - i - 1)
            tmp2 = check[i+1:]
            print(int(tmp1, 2) - int(tmp2, 2))
            break
