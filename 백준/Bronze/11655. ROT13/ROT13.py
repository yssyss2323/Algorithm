s = input()

small = [chr(i) for i in range(97, 123)]
large = [chr(i) for i in range(65, 91)]

ans = ''
for ch in s:
    for i in range(26):
        if ch == large[i]:
            ans += large[(i + 13) % 26]
            break
        elif ch == small[i]:
            ans += small[(i + 13) % 26]
            break
    else:
        ans += ch
print(ans)