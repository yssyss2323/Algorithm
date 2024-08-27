s = input()
p = input()

length = len(p)
ans = 0
while p:
    idx = 0
    while idx + 1 <= length and p[:idx + 1] in s:
        idx += 1
    p = p[idx:]
    ans += 1
print(ans)
