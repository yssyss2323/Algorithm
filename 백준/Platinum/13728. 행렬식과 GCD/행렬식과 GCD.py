from math import gcd

n = int(input())

fibo_table = [1, 1]
for i in range(2, n + 2):
    tmp = fibo_table[i - 1] + fibo_table[i - 2]
    tmp %= 10 ** 9 + 7
    fibo_table.append(tmp)

ans = 0
for i in range(1, n + 1):
    tmp = gcd(i + 1, n + 1)
    ans += fibo_table[tmp - 1]
    ans %= 10 ** 9 + 7
print(ans)
