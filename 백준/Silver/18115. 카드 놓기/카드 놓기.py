from collections import deque

n = int(input())
skills = list(map(int, input().split()))
cards = deque()

for i, skill in enumerate(skills[::-1]):  # i+1 카드 내려놓을때 skill 사용
    if skill == 1:
        cards.appendleft(i + 1)
    elif skill == 2:
        tmp = cards.popleft()
        cards.appendleft(i + 1)
        cards.appendleft(tmp)
    else:
        cards.append(i + 1)

print(*cards)