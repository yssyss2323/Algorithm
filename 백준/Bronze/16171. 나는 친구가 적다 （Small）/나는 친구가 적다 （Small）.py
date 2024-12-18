s = input()
k = input()

prep = ''
for ch in s:
    if ch not in '1234567890':
        prep += ch

print(1 if k in prep else 0)