n = int(input())
slist = list(map(int, input().split()))

candidates = set()
for i in range(1, 2 ** n):
    check = bin(i)[2:]
    check = (n - len(check)) *'0' + check
    tot = 0
    for j in range(n):
        if check[j] == '1':
            tot += slist[j]
    candidates.add(tot)

for i in range(1, sum(slist) + 2):
    if i not in candidates:
        print(i)
        break