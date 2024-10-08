from itertools import combinations


def calculate_team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += synergy[team[i]][team[j]]
    return score


n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

synergy = [[table[i][j] + table[j][i] for j in range(n)] for i in range(n)]

players = list(range(1, n))
half_team_size = n // 2
min_diff = float('inf')

for team1_rest in combinations(players, half_team_size - 1):
    team1 = [0] + list(team1_rest)
    team2 = [i for i in range(n) if i not in team1]

    team1_score = calculate_team_score(team1)
    team2_score = calculate_team_score(team2)

    diff = abs(team1_score - team2_score)
    if diff < min_diff:
        min_diff = diff
        if min_diff == 0:
            break

print(min_diff)
