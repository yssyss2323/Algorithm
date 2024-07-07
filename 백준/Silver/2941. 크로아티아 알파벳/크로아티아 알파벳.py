word = input()
length = len(word)
word += 'xxx'
ans = 0
idx = 0
while idx < length:
    if word[idx:idx+2] in ('c=','c-','d-','lj','nj','s=','z='):
        ans += 1
        idx += 2
    elif word[idx:idx+3] == 'dz=':
        ans += 1
        idx += 3
    else:
        ans += 1
        idx += 1
print(ans)