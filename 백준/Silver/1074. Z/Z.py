n, r, c = map(int, input().split())

answer = 0
for i in reversed(range(n)):
    answer += ((r // 2 ** i) * 2 + c // 2 ** i) * 4 ** i
    r, c = r % 2 ** i, c % 2 ** i
print(answer)