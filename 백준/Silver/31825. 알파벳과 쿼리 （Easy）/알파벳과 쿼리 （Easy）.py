import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()

def counting(string):
    cnt = 1
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            cnt += 1
    return cnt

for _ in range(q):
    m, l, r = map(int, input().split())
    if m == 1:
        print(counting(s[l - 1:r]))
    else:
        tmp = ""
        for ch in s[l - 1:r]:
            if ch == 'Z':
                tmp += 'A'
            else:
                tmp += chr(ord(ch) + 1)
        s = s[:l - 1] + tmp + s[r:]
        