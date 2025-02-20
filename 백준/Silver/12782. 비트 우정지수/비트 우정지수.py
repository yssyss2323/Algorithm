import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = input().split()
    check = {'1':0, '0':0}
    for i in range(len(n)):
        nn, mm = n[i], m[i]
        if nn != mm:
            check[nn] += 1
    print(max(check['0'], check['1']))