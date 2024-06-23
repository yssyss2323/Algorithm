def d(n):
    for ch in str(n):
        n += int(ch)
    return n


numlist = [False] + [True] * 10000
for i in range(1, 10001):
    tmp = d(i)
    if tmp <= 10000:
        numlist[d(i)] = False
for num in range(1, 10001):
    if numlist[num]:
        print(num)
