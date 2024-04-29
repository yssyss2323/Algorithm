def f(x):
    return 1 + 3 * x * (x - 1)


n = int(input())
answer = 1
while f(answer) < n:
    answer += 1
print(answer)