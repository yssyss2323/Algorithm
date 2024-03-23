k = int(input())
bignum = 7500000
prime = [False] * 2 + [True] * (bignum-1)
primelist = []
for i in range(2,bignum+1):
    if prime[i]:
        primelist.append(i)
        if len(primelist) == k:
            break
        for j in range(i*2,bignum+1,i):
            prime[j] = False
print(primelist[-1])