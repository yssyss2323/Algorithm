n = int(input())
dice = list(map(int,input().split()))
one_min = min(dice)
two = []
for tup in [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,4),(3,4),(5,1),(5,2),(5,3),(5,4)]:
    two.append(dice[tup[0]] + dice[tup[1]])
two_min = min(two)
three = []
for tup in [(0,1,2),(0,1,3),(0,2,4),(0,3,4),(5,1,2),(5,1,3),(5,2,4),(5,3,4)]:
    three.append(dice[tup[0]] + dice[tup[1]] + dice[tup[2]])
three_min = min(three)

if n == 1:
    tmp = 0
    for i in dice:
        tmp += i
    print(tmp - max(dice))
else:
    answer = one_min * (n - 2) * (5 * n - 6) + two_min * (2 * n - 3) * 4 + three_min * 4
    print(answer)