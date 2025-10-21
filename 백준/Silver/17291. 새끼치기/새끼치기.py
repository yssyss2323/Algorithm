n = int(input())
worms = [0] * n
worms[0] = 1

for i in range(1, n):
    worms[i] = sum(worms)
    if (i - 3) % 2 == 0:
        if i - 3 >= 0:
            worms[i - 3] = 0
    if (i - 4) % 2:
        if i - 4 >= 0:
            worms[i - 4] = 0
print(sum(worms))