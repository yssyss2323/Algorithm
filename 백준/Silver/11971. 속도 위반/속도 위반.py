N, M = map(int, input().split())

law, record = dict(), dict()
for i in range(1, 101):
    law[i] = 0
    record[i] = 0

idx = 1
for _ in range(N):
    l, d = map(int, input().split())
    for i in range(idx, idx + l):
        law[i] = d
    idx += l

idx = 1
for _ in range(M):
    s, v = map(int, input().split())
    for i in range(idx, idx + s):
        record[i] = v
    idx += s

maximum = 0
for i in range(1, 101):
    tmp = record[i] - law[i]
    if tmp > maximum:
        maximum = tmp
print(maximum)
