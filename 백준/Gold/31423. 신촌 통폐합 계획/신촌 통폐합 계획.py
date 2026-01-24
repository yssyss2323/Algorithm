import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
names = [input() for _ in range(n)]

arr = {i:0 for i in range(1, n + 1)}
tails = {i: i for i in range(1, n + 1)}
cand = set(range(1, n + 1))
for _ in range(n - 1):
    i, j = map(int, input().split())
    i_tail = tails[i]
    cand.remove(j)
    arr[i_tail] = j
    tails[i] = tails[j]

start = cand.pop()
anslist = [start]
while arr[start]:
    start = arr[start]
    anslist.append(start)

print("".join([names[x - 1] for x in anslist]))