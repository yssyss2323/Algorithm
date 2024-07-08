t = int(input())
for _ in range(t):
    money = int(input())
    q, money = divmod(money, 25)
    d, money = divmod(money, 10)
    n, p = divmod(money, 5)
    print(q,d,n,p)