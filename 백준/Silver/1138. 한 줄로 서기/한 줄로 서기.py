n = int(input())
tall_left = list(map(int, input().split()))
pos = []
for i in reversed(range(n)):
    x = tall_left[i]
    pos = pos[:x] + [i + 1] + pos[x:]
print(*pos)