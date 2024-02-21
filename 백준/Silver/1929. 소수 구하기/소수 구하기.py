m,n = map(int,input().split())
prime = [False]*2 + [True] * (n-1)
for i in range(2,n+1):
    if prime[i]:
        for j in range(i,n+1,i):
            prime[j] = False
        prime[i] = True
for i in range(m,n+1):
    if prime[i]:
        print(i)