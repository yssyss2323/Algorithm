secret = list(map(int, input()))
k = int(input())
n = len(secret)

numlist = []
for i in range(n):
    if secret[i] in [1, 2, 6, 7]:
        numlist.append(i)
num = len(numlist)

kk = bin(k - 1)[2:]
if num - len(kk) < 0:
    print(-1)
else:
    kk = (num - len(kk)) * '0' + kk
    for i in range(num):
        if kk[i] == '0' and secret[numlist[i]] in [6, 7]:
            secret[numlist[i]] %= 5
        if kk[i] == '1' and secret[numlist[i]] in [1, 2]:
            secret[numlist[i]] += 5
    print(*secret, sep='')