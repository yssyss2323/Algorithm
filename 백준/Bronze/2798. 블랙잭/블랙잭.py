n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if m - answer > m - (cards[i] + cards[j] + cards[k]) >= 0:
                answer = cards[i] + cards[j] + cards[k]
print(answer)
