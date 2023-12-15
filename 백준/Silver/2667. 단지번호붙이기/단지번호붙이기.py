import sys
sys.setrecursionlimit(10**6)

n = int(input())

# 지도 초기화 : 집 있는 곳 은 True, 빈 곳은 False로
field = [[False]*n for _ in range(n)]
for i in range(n):
    string = input()
    for j in range(len(string)):
        if string[j] == '1':
            field[i][j] = True

# dfs 이동방향
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# dfs 함수 : field의 상하좌우 방향을 탐색하여 True 영역 넓이 카운트
def dfs(x,y):
    field[x][y] = False
    area = 1
    for i in range(4):
        newx, newy = x+dx[i], y+dy[i]
        if 0 <= newx < n and 0 <= newy < n and field[newx][newy]:
            area += dfs(newx,newy)
    return area

# 정답 출력
answerlist = []
for i in range(n):
    for j in range(n):
        if field[i][j]:
            answerlist.append(dfs(i,j))
answerlist.sort()
print(len(answerlist))
for i in answerlist:
    print(i)