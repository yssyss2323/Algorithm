import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
words = [input() for _ in range(n)]
check = dict()
for word in words:
    tmp = ''
    for ch in word:
        tmp += ch
        check[tmp] = check.get(tmp,0) + 1

shared, max_length = '', 0
for a,b in check.items():
    tmp_length = len(a)
    if b > 1:
        if tmp_length > max_length:
            shared = a
            max_length = tmp_length

cnt = 0
for word in words:
    if shared == word[:max_length]:
        cnt += 1
        print(word)
    if cnt == 2:
        break
else:
    print(words[0])
    print(words[1])
