import sys
input = lambda:sys.stdin.readline().rstrip()

s = input()

check = [[] for _ in range(len(s))]
tmp = [0 for _ in range(ord('z') - ord('a') + 1)]

for i in range(len(s)):
    ch = s[i]
    tmp[ord(ch) - ord('a')] += 1
    check[i] = tmp[:]

for _ in range(int(input())):
    a, l, r = input().split()
    ord_num = ord(a) - ord('a')
    if l == '0':
        print(check[int(r)][ord_num])
    else:
        print(check[int(r)][ord_num] - check[int(l) - 1][ord_num])
