m = int(input())
n = int(input())

prime = [False] * 2 + [True] * (n - 1)
for i in range(2, n + 1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

anslist = []
for i in range(m, n + 1):
    if prime[i]:
        anslist.append(i)
if anslist:
    print(sum(anslist))
    print(anslist[0])
else:
    print(-1)