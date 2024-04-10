n = int(input())

# 루트n 이하 소인수 탐색
yes_prime = set()
m = n
i = 2
while i ** 2 <= m:
    if m % i:
        i += 1
    else:
        m //= i
        yes_prime.add(i)
if m > 1:
    yes_prime.add(m)

# n이하 서로소 개수
for i in yes_prime:
    n //= i
    n *= i - 1
print(n)