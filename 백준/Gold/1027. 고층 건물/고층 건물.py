N = int(input())
buildings = list(map(int, input().split()))

answer = 0
for i in range(N):
    right = buildings[i + 1:]
    right_max, right_see = -float("inf"), 0
    for j, height in enumerate(right):
        grad = (height - buildings[i]) / (j + 1)
        if grad > right_max:
            right_max = grad
            right_see += 1

    left = buildings[:i]
    left_max, left_see = -float("inf"), 0
    for j, height in enumerate(reversed(left)):
        grad = (height - buildings[i]) / (j + 1)
        if grad > left_max:
            left_max = grad
            left_see += 1
    if answer < right_see + left_see:
        answer = right_see + left_see
print(answer)
