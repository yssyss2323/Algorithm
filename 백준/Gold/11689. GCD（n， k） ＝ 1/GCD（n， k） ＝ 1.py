n = int(input())

# 루트n 이하 소인수 탐색
yes_prime = []
m = n
for i in range(2, int(m ** 0.5) + 1):
    if m % i:
        continue
    else:
        yes_prime.append(i)
        while m % i == 0:
            m //= i
if m > 1:
    yes_prime.append(m)

# n이하 서로소 개수
for i in yes_prime:
    n //= i
    n *= i - 1
print(n)
