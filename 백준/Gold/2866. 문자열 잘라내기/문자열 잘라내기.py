import sys
input = sys.stdin.readline

r, c = map(int, input().split())

words = list(map(''.join, zip(*[input().rstrip() for _ in range(r)])))

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