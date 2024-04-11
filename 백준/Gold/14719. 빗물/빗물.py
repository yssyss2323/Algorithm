h, w = map(int, input().split())
world = [[0 for _ in range(h)] for _ in range(w)]
blocks = list(map(int, input().split()))

for i in range(w):
    for j in range(blocks[i]):
        world[i][j] = 1

now_water = h * w - sum(blocks)
height = h - 1
while not (world[0][height] and world[-1][height]):
    left, right = w, 0
    for i in range(w):
        if world[i][height]:
            left = i
            break
    now_water -= left
    for i in reversed(range(w)):
        if world[i][height]:
            right = i
            break
    if right:
        now_water -= w - right - 1
    height -= 1
    if height < 0:
        break
print(now_water)
