n = int(input())
s = input()

p = s.count('P')
c = s.count('C')
cnt = min(p, c)

ans = ""
pcnt, ccnt = 0, 0
for ch in s:
    if ch == 'P' and pcnt < cnt:
        ans += 'C'
        pcnt += 1
    elif ch == 'C' and ccnt < cnt:
        ans += 'P'
        ccnt += 1
    else:
        ans += ch
print(ans)