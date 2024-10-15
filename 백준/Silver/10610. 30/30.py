n = list(map(int, input()))
if sum(n) % 3 == 0 and 0 in n:
    n.sort(reverse=True)
    print(*n, sep='')
else:
    print(-1)