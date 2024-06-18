from collections import deque

s = list(map(ord, input()))

# 중요 인덱스 탐색
x = s[::-1]
indexlist = deque()
while x:
    idx = x.index(min(x))
    indexlist.appendleft(len(x) - idx - 1)
    x = x[idx + 1:]
indexlist.popleft()

# 프로세스 : 중요인덱스 이전에서 반전 + 중요인덱스에서 반전
for i in indexlist:
    tmp1 = s[:i]
    tmp2 = s[i:]
    s = tmp1[::-1] + tmp2

    tmp3 = s[:i + 1]
    tmp4 = s[i + 1:]
    s = tmp3[::-1] + tmp4

answer = ''
for i in s:
    answer += chr(i)
print(answer)
