def c(n, m):  # n개 중에서 m개를 뽑는 경우의 수를 나타내는 함수
    if m == 1:
        return [[i] for i in range(1, n + 1)]
    elif n == m:
        return [list(range(1, n + 1))]
    else:
        tmp = c(n - 1, m) + [i + [n] for i in c(n - 1, m - 1)]
        tmp.sort()
        return tmp

while 1:
    tmp = list(map(int, input().split()))
    if len(tmp) == 1:
        break
    else:
        num = tmp[0]
        numlist = tmp[1:]
        for i in c(num, 6):
            answerlist = [numlist[i[j] - 1] for j in range(6)]
            print(*answerlist)
        print('')