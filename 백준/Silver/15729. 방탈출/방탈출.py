n = int(input())
state = list(map(int, input().split())) + [0, 0]

ans = 0
for i in range(n):
    if state[i] == 1:
        ans += 1
        state[i] = 0
        state[i + 1] = (state[i + 1] + 1) % 2
        state[i + 2] = (state[i + 2] + 1) % 2
print(ans)