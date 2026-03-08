arr = [int(input()) for _ in range(10)]
ans = 0
for i in range(10):
    curr = sum(arr[:i + 1])
    if abs(curr - 100) < abs(ans - 100):
        ans = curr
    elif abs(curr - 100) == abs(ans - 100) and curr > ans:
        ans = curr
print(ans)
