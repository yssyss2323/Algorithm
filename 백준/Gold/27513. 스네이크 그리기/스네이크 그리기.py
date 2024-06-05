n, m = map(int, input().split())

num = 0
snake = []
if n % 2 == 0:
    num = n * m
    for i in range(1, n + 1):
        snake.append([i, 1])
    for i in range(n):
        for j in range(2, m + 1):
            if i % 2 == 0:
                snake.append([n - i, j])
            else:
                snake.append([n - i, m + 2 - j])
elif m % 2 == 0:
    num = n * m
    for i in range(1, m + 1):
        snake.append([1, i])
    for i in range(m):
        for j in range(2, n + 1):
            if i % 2 == 0:
                snake.append([j, m - i])
            else:
                snake.append([n + 2 - j, m - i])
else:
    num = n * m - 1
    for i in range(1, m + 1):
        snake.append([1, i])
    for i in range(m - 2):
        for j in range(2, n + 1):
            if i % 2 == 0:
                snake.append([j, m - i])
            else:
                snake.append([n + 2 - j, m - i])
    for i in range(n - 2):
        if i % 2 == 0:
            snake.append([n - i, 2])
            snake.append([n - i, 1])
        else:
            snake.append([n - i, 1])
            snake.append([n - i, 2])
    snake.append([2, 1])

print(num)
for i in snake:
    print(*i)
