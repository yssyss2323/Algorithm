def C(n, m):
    if m == 1:
        return [[i] for i in range(1, n + 1)]
    elif n == m:
        return [list(range(1, n + 1))]
    else:
        tmp = [i + [n] for i in C(n - 1, m - 1)]
        tmp += C(n - 1, m)
        tmp.sort()
        return tmp


l, c = map(int, input().split())
english = list(input().split())
english.sort()

for i in C(c, l):
    answer = []
    tmp = 0
    for j in i:
        answer.append(english[j - 1])
    for k in answer:
        if k in 'aeiou':
            tmp += 1
    if tmp >= 1 and l - tmp >= 2:
        print(*answer,sep='')