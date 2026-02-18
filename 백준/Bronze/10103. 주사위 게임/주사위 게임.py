n = int(input())
score = [100, 100]
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        score[0] -= b
    elif a > b:
        score[1] -= a
print(score[0])
print(score[1])