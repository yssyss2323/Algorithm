import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
field = []
height = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    field.append(tmp)
    for i in tmp:
        if i not in height:
            height.append(i)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dfs 함수 : visited[x][y]에서 시작하여 주변의 k보다 큰 값을 0으로 바꾼다
def dfs(x, y, k):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = 0
        for i in range(4):
            newx, newy = x + dx[i], y + dy[i]
            if 0 <= newx < n and 0 <= newy < n and visited[newx][newy] > k:
                stack.append((newx, newy))

answerlist = [1] # 1은 아무지역도 물에 안잠긴 경우를 의미
for h in height:
    answer = 0
    visited = [[x for x in row] for row in field]
    for i in range(n):
        for j in range(n):
            if visited[i][j] > h:
                dfs(i, j, h)
                answer += 1
    answerlist.append(answer)
print(max(answerlist))