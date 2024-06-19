import sys

input = sys.stdin.readline

n = int(input())
check = dict()
for _ in range(n):
    name, state = input().split()
    check[name] = True if state == 'enter' else False

anslist = []
for name, state in check.items():
    if state:
        anslist.append(name)
anslist.sort(reverse=True)
print(*anslist, sep='\n')
