n, m = map(int, input().split())

xset, yset = set(), set()
for i in range(n):
    tmp = input()
    if 'X' in tmp:
        xset.add(i)
        for j in range(m):
            if tmp[j] == 'X':
                yset.add(j)

print(max(n - len(xset), m - len(yset)))