s = input()
ans = ''
while s:
    if s[0] == '.':
        s = s[1:]
        ans += '.'
    else:
        if len(s) >= 4 and s[:4] == 'XXXX':
            ans += 'AAAA'
            s = s[4:]
        elif len(s) >= 2 and s[:2] == 'XX':
            ans += 'BB'
            s = s[2:]
        else:
            print(-1)
            break
else:
    print(ans)