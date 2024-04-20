N = int(input())
pair, order = [list(map(int, input().split()))], [1]
for _ in range(N - 1):
    x, y = map(int, input().split())
    ord = 1
    for i in range(len(pair)):
        a, b = pair[i]
        if x < a and y < b:
            ord += 1
        elif x > a and y > b:
            order[i] += 1
    pair.append([x, y])
    order.append(ord)
print(*order)
