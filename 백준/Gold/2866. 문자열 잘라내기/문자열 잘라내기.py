import sys
input = sys.stdin.readline

r, c = map(int, input().split())

words = [''] * c
for _ in range(r):
    tmp = input()
    for i in range(c):
        words[i] += tmp[i]

cnt = 0
for i in range(1, r):
    check = set()
    for j in range(c):
        check.add(words[j][i:])
    if len(check) < c:
        print(cnt)
        break
    else:
        cnt += 1
else:
    print(cnt)