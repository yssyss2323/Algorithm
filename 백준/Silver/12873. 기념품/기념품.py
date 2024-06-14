N = int(input())
q = list(range(1, N + 1))
now = N
for i in range(N - 1):
    tmp = (i + 1) ** 3 % now - 1
    if tmp < 0: tmp = now - 1
    q = q[tmp + 1:] + q[:tmp]
    now -= 1
print(q[0])
