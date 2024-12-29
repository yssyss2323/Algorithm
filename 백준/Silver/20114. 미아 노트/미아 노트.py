n, h, w = map(int, input().split())

arr = [input() for _ in range(h)]
ans = ''
for i in range(n):
    tmp = ''
    for j in range(h):
        tmp += arr[j][i * w:i * w + w]
    tmp = set(tmp)
    if len(tmp) == 1:
        ans += tmp.pop()
    else:
        tmp.discard('?')
        ans += tmp.pop()
print(ans)