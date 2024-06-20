na, nb = map(int, input().split())
alist = set(map(int, input().split()))
blist = set(map(int, input().split()))
anslist = list(alist.difference(blist))
if anslist:
    anslist.sort()
    print(len(anslist))
    print(*anslist)
else:
    print(0)
