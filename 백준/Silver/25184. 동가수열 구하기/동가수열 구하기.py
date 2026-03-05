n = int(input())
ans = []
if n % 2:
    left = [i for i in range(1, n // 2 + 1)]
    right = [i for i in range(n // 2 + 2, n + 1)]
    for i in range(n // 2):
        ans.append(left[i])
        ans.append(right[i])
    if n % 2:
        ans.append(n // 2 + 1)
else:
    left = [i for i in range(1, n // 2)]
    right = [i for i in range(n // 2 + 2, n + 1)]
    ans.append(n // 2 + 1)
    for i in range(n // 2 - 1):
        ans.append(left[i])
        ans.append(right[i])
    ans.append(n // 2)

print(*ans)