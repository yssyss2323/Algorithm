from collections import deque

n, k, m = map(int, input().split())

q = deque(list(range(1, n + 1)))
cnt = 0
while q:
    if cnt == m:
        k *= -1
        cnt = 0
    if k > 0:
        q.rotate(-k)
    else:
        q.rotate(-k - 1)
    print(q.pop())
    cnt += 1
