s = input()
cnt_one = s.count('1')
cnt_zero = len(s) - cnt_one

cnt = 0
tmp = ''
for ch in s:
    if cnt < cnt_one // 2 and ch == '1':
        cnt += 1
    else:
        tmp += ch

cnt = 0
ans = ''
for ch in reversed(tmp):
    if cnt < cnt_zero // 2 and ch == '0':
        cnt += 1
    else:
        ans += ch

print(ans[::-1])