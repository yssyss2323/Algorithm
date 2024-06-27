from collections import deque

t,m,n = map(int, input().split())

def f(x):
    value = int(x) - m
    return value if value >= 0 else 60 + value

information = []
trains = []
total_cnt = 0
for _ in range(t):
    tmp = input().split()
    total_cnt += len(tmp) - 2
    trains.append(tmp[0])
    tmp = list(map(f, tmp[1:-1]))
    tmp.sort()
    information.append(deque(tmp))
n %= total_cnt
if n == 0:
    n = total_cnt
for i in range(n):
    minimum = 60
    idx = -1
    for j in range(len(information)):
        if information[j]:
            val = int(information[j][0])
            if val < minimum:
                minimum = val
                idx = j
    information[idx].popleft()
print(trains[idx])