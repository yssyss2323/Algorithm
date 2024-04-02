from collections import Counter

n = int(input())
cards = Counter(list(map(int,input().split())))
m = int(input())
wanted = list(map(int,input().split()))
answer = []
for i in wanted:
    answer.append(cards[i])
print(*answer)