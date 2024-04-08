# x99..9(9는 n개) 이하까지의 숫자를 카운팅
def counting(x, n):
    tmp = n * 10 ** (n - 1)
    for i in range(10):
        check[i] += tmp * (x + 1)
    for i in range(x + 1):
        check[i] += 10 ** n

check = [0 for _ in range(10)]
N = input()
length = len(N)

for i in range(length - 1):
    a, b = int(N[i]) - 1, length - i - 1
    if a != -1:
        counting(a, b)
    check[int(N[i])] += int(N[i + 1:]) + 1
last = int(N[length - 1])
for i in range(last + 1):
    check[i] += 1
check[0] -= int('1' * length)
print(*check)
