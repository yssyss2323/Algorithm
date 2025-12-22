import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
curr = [[n // 2 - 1, n // 2 - 1], [n // 2, n // 2]]
direction = 'UDLR'

def check(curr):
    x1, y1 = curr[0]
    x2, y2 = curr[1]

    u = False if x1 == 0 or sum(arr[x1 - 1][y1:y2 + 1]) <= 0 else sum(arr[x1 - 1][y1:y2 + 1])
    d = False if x2 == n - 1 or sum(arr[x2 + 1][y1:y2 + 1]) <= 0 else sum(arr[x2 + 1][y1:y2 + 1])
    l = False if y1 == 0 or sum([arr[t][y1 - 1] for t in range(x1, x2 + 1)]) <= 0 else sum([arr[t][y1 - 1] for t in range(x1, x2 + 1)])
    r = False if y2 == n - 1 or sum([arr[t][y2 + 1] for t in range(x1, x2 + 1)]) <= 0 else sum([arr[t][y2 + 1] for t in range(x1, x2 + 1)])

    return [u, d, l, r]


score = 0
ans = ""
while True:
    tmp_score = 0
    tmp_ch = ''
    for i in range(4):
        if check(curr)[i] and check(curr)[i] > tmp_score:
            tmp_score = check(curr)[i]
            tmp_ch = direction[i]
    if tmp_ch:
        score += tmp_score
        ans += tmp_ch
        if tmp_ch == "U":
            curr[0][0] -= 1
        elif tmp_ch == "D":
            curr[1][0] += 1
        elif tmp_ch == "L":
            curr[0][1] -= 1
        else:
            curr[1][1] += 1
    else:
        print(score)
        print(ans)
        break