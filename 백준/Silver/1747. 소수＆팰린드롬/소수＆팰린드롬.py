def check_pelindrom(n):
    m = str(n)
    return m == m[::-1]


MAXIMUM = 1003001  # 체로 100만 이상인 조건 충족하는 수를 찾았음
n = int(input())
prime = [False] * 2 + [True] * (MAXIMUM - 1)
for i in range(2, MAXIMUM + 1):
    if prime[i]:
        for j in range(2 * i, MAXIMUM + 1, i):
            prime[j] = False

for i in range(n, MAXIMUM + 1):
    if prime[i] and check_pelindrom(i):
        print(i)
        break
