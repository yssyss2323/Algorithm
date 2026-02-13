check = {i - ord('A') + 1:chr(i) for i in range(ord('A'), ord('Z') + 1)}

while True:
    string = input()
    r = int(string[string.index('R') + 1:string.index('C')])
    c = int(string[string.index('C') + 1:])
    if (r, c) == (0, 0):
        break

    cc = ""
    while c > 26:
        tmp = c % 26 if c % 26 else 26
        cc += check[tmp]
        c -= tmp
        c //= 26
    tmp = c % 26 if c % 26 else 26
    cc += check[tmp]
    cc = cc[::-1]
    print(cc + str(r))