def dfs(x):
    if possible_table[x]:
        answer = gain[x]
        tmplist = []
        for i in range(x, N):
            if relation_table[x][i]:
                tmplist.append(dfs(i))
        if tmplist:
            answer += max(tmplist)
    else:
        answer = 0
    return answer

N = int(input())
gain = [0] * N
relation_table = [[True] * N for _ in range(N)]
possible_table = [True] * N
for i in range(N):
    t, p = map(int, input().split())
    if i + t > N:
        possible_table[i] = False
    for j in range(min(i + t, N)):
        relation_table[i][j] = False
    gain[i] = p

answerlist = []
for i in range(N):
    answerlist.append(dfs(i))
answer = max(answerlist)
print(answer)
