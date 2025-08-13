from collections import deque

a, k = map(int, input().split())
check = {a}
q = deque([(a, 0)])

while True:
    curr, cnt = q.popleft()
    if curr > k:
        continue
    if curr + 1 == k or curr * 2 == k:
        print(cnt + 1)
        break
    if curr + 1 not in check:
        check.add(curr + 1)
        q.append((curr + 1, cnt + 1))
    if curr * 2 not in check:
        check.add(curr * 2)
        q.append((curr * 2, cnt + 1))