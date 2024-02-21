n = int(input())
cards = list(range(1,n+1))
answer = []
for _ in range(n-1):
    answer.append(cards[0])
    del cards[0]
    cards = cards[1:] + [cards[0]]
answer += [cards[0]]
print(*answer)