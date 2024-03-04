n = int(input())
x = n // 5
for i in range(x, -1, -1):
    if (n - i * 5) % 2:
        continue
    else:
        j = (n - i * 5) // 2
    print(i + j)
    break
else:
    print(-1)