from collections import deque

N = int(input())
q = deque(range(1, N + 1))
now = N
for i in range(N - 1):
    tmp = (i + 1) ** 3 % now - 1
    q.rotate(-tmp)
    q.popleft()
    now -= 1
print(q[0])
