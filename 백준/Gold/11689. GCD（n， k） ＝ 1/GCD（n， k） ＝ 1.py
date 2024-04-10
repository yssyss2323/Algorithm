n = int(input())

# 루트n 이하 소수 탐색
root_n = int(n**0.5)
check = [False] * 2 + [True] * (root_n - 1)
prime = []
for i in range(root_n+1):
    if check[i]:
        prime.append(i)
        for j in range(i*2,root_n+1,i):
            check[j] = False

# 루트n 이하 소인수 탐색
yes_prime = []
m = n
while prime:
    tmp = prime.pop()
    if m % tmp == 0:
        while m % tmp == 0:
            m //= tmp
        yes_prime.append(tmp)
if m > 1:
    yes_prime.append(m)

# n이하 서로소 개수
for i in yes_prime:
    n //= i
    n *= i - 1
print(n)