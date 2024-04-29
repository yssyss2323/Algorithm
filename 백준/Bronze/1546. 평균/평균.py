N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
total = 0
for score in scores:
    total += score
real_avg = total / N
fake_avg = real_avg * 100 / M
print(fake_avg)