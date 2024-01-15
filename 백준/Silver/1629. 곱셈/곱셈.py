a, b, c = map(int, input().split())
a %= c
check = [0] * 31
check[0] = a
for i in range(1, 31):
    check[i] = check[i - 1] ** 2 % c
answer = 1
for idx, i in enumerate(reversed((bin(b)[2:]))):
    if i == '1':
        answer *= check[idx]
        answer %= c
print(answer)