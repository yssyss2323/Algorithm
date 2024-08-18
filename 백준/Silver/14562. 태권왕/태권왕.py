from collections import deque

n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    visited = set()
    q = deque([(s, t, 0)])
    while q:
        curr_s, curr_t, cnt = q.popleft()
        if curr_s == curr_t:
            print(cnt)
            break
        if curr_s + 1 <= curr_t and (curr_s + 1, curr_t) not in visited:
            visited.add((curr_s + 1, curr_t))
            q.append((curr_s + 1, curr_t, cnt + 1))
        if curr_s * 2 <= curr_t + 3 and (curr_s * 2, curr_t + 3) not in visited:
            visited.add((curr_s * 2, curr_t + 3))
            q.append((curr_s * 2, curr_t + 3, cnt + 1))