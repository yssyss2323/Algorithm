def find_num(n):
    check = '9876543210'
    nn = '0' * (10 - len(bin(n + 1)[2:])) + bin(n + 1)[2:]
    ans = ''
    for i in range(10):
        if nn[i] == '1':
            ans += check[i]
    return int(ans)

n = int(input())
if n >= 1023:
    print(-1)
else:
    check = []
    for i in range(1023):
        check.append(find_num(i))
    check.sort()
    print(check[n])