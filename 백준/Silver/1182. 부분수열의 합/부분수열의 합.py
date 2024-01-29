n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for i in range(1, 2 ** n):
    tmp1 = bin(i)[2:]
    tmp2 = list(map(int, '0' * (n - len(tmp1)) + tmp1))
    tmp3 = 0
    for j in range(n):
        tmp3 += numbers[j] * tmp2[j]
    if tmp3 == s:
        answer += 1
print(answer)