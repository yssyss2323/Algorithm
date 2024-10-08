def score(team):
    num = len(team)
    ans = 0
    for i in range(num):
        for j in range(num):
            ans += table[team[i]][team[j]]
    return ans


def bt(check):
    global ans
    if len(check) == n:
        team1, team2 = [], []
        for i in range(n):
            if check[i] == 1:
                team1.append(i)
            else:
                team2.append(i)
        tmp = abs(score(team1) - score(team2))
        # print(team1, team2, score(team1), score(team2))
        if ans > tmp:
            ans = tmp

    else:
        if sum(check) < n // 2:
            check.append(1)
            bt(check)
            check.pop()
        if len(check) - sum(check) < n // 2:
            check.append(0)
            bt(check)
            check.pop()



n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
bt([])
print(ans)
