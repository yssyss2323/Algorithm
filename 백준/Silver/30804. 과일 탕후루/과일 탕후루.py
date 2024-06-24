from collections import deque

n = int(input())
tanghuru = list(map(int, input().split())) + [0]

start, end = 0, 0

ans = 0
tmp = {tanghuru[0]: 1}
tmp2 = deque([tanghuru[0]])
while end < n:
    if len(tmp) <= 2:
        if end - start + 1 > ans:
            ans = end - start + 1
        end += 1
        tmp[tanghuru[end]] = tmp.get(tanghuru[end], 0) + 1
        tmp2.append(tanghuru[end])
    else:
        start += 1
        first = tmp2[0]
        if tmp[first] > 1:
            tmp[first] -= 1
        else:
            tmp.pop(first)
        tmp2.popleft()
print(ans)
