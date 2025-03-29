n = int(input())

color = [1] * (n + 1)
curr_color = 1
for i in range(2, n + 1):
    if color[i] == 1:
        curr_color += 1
        for j in range(i, n + 1, i):
            color[j] = curr_color

print(curr_color)
print(*color[1:])