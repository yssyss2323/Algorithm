import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = {'kor':{'apple':{'red':0, 'blue':0, 'green':0}, 'pear':{'red':0, 'blue':0, 'green':0}, 'orange':{'red':0, 'blue':0, 'green':0}},
           'eng':{'apple':{'red':0, 'blue':0, 'green':0}, 'pear':{'red':0, 'blue':0, 'green':0}, 'orange':{'red':0, 'blue':0, 'green':0}},
           'math':{'apple':{'red':0, 'blue':0, 'green':0}, 'pear':{'red':0, 'blue':0, 'green':0}, 'orange':{'red':0, 'blue':0, 'green':0}}}

for _ in range(n):
    s, f, c = input().split()
    check[s][f][c] += 1

for _ in range(m):
    s, f, c = input().split()
    tmp = 0
    if s == '-':
        for ss in ['kor', 'eng', 'math']:
            if f == '-':
                for ff in ['apple', 'pear', 'orange']:
                    if c == '-':
                        for cc in ['red', 'blue', 'green']:
                            tmp += check[ss][ff][cc]
                    else:
                        tmp += check[ss][ff][c]
            else:
                if c == '-':
                    for cc in ['red', 'blue', 'green']:
                        tmp += check[ss][f][cc]
                else:
                    tmp += check[ss][f][c]
    else:
        if f == '-':
            for ff in ['apple', 'pear', 'orange']:
                if c == '-':
                    for cc in ['red', 'blue', 'green']:
                        tmp += check[s][ff][cc]
                else:
                    tmp += check[s][ff][c]
        else:
            if c == '-':
                for cc in ['red', 'blue', 'green']:
                    tmp += check[s][f][cc]
            else:
                tmp = check[s][f][c]
    print(tmp)