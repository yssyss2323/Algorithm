n = int(input())
card1 = [int(input()) for _ in range(n // 2)]
card2 = [int(input()) for _ in range(n // 2)]
card1.sort()
card2.sort()
my_card = list(set(range(1,2*n+1)).difference(card1 + card2))
my_card1 = my_card[n//2:]
my_card2 = my_card[:n//2]

cnt = 0
idx1, idx2 = 0, 0
while idx1 < n // 2:
    if my_card1[idx1] < card1[idx2]:
        idx1 += 1
    else:
        cnt += 1
        idx1 += 1
        idx2 += 1
idx1, idx2 = 0, 0
while idx2 < n // 2:
    if my_card2[idx1] < card2[idx2]:
        idx1 += 1
        idx2 += 1
        cnt += 1
    else:
        idx2 += 1

print(cnt)
