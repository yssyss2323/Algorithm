N = int(input())
card_nums = set(map(int, input().split()))

M = int(input())
given_nums = list(map(int, input().split()))

answer = []
for num in given_nums:
    if num in card_nums:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)
