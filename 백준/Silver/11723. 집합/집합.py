import sys
input = lambda: sys.stdin.readline().rstrip()

S = set()
M = int(input())
for _ in range(M):
    order = input()
    if order == 'all':
        S = set(range(1, 21))
    elif order == 'empty':
        S = set()
    else:
        order, x = order.split()
        x = int(x)
        if order == 'add':
            S.add(x)
        elif order == 'remove':
            S.discard(x)
        elif order == 'check':
            print(1 if x in S else 0)
        else:
            if x in S:
                S.remove(x)
            else:
                S.add(x)
