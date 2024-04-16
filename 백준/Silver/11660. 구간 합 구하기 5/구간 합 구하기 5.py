import sys
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
table = []
first = list(map(int,input().split()))
for i in range(1,n):
    first[i] += first[i-1]
table.append(first)
for i in range(1,n):
    tmp = list(map(int,input().split()))
    for j in range(1,n):
        tmp[j] += tmp[j-1]
    for j in range(n):
        tmp[j] += table[i-1][j]
    table.append(tmp)
table = [[0] * n] + table
for i in range(n+1):
    table[i] = [0] + table[i]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1])