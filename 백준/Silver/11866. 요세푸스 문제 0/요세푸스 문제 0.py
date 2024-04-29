n, k = map(int, input().split())
stack = list(map(str, range(1, n + 1)))
answer = []
while stack:
    key = (k - 1) % len(stack)
    answer.append(stack[key])
    stack = stack[key + 1:] + stack[:key]
print(f"<{', '.join(answer)}>")
