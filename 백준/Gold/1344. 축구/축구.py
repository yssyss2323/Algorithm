prime = [2,3,5,7,11,13,17]

def comb(m,n):
    if n == 1:
        return m
    elif m == n:
        return 1
    else:
        return comb(m-1,n-1) + comb(m-1,n)

def possible(x):
    x /= 100
    poss = 0
    for i in prime:
        poss += comb(18,i)*x**i*(1-x)**(18-i)
    return poss

a = int(input())
b = int(input())
answer = possible(a) + possible(b) - possible(a)*possible(b)
print(answer)