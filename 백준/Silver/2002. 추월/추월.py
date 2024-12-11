import sys
input = sys.stdin.readline

n = int(input())
tf = dict()
for i in range(n):
    tf[input()] = i

state = [0] * n
for i in range(n):
    state[tf[input()]] = i
ans = 0
stand = -1
for i in range(n - 1):
    if state[i] > stand:
        stand = state[i]
    if stand > state[i + 1]:
        ans += 1
print(ans)