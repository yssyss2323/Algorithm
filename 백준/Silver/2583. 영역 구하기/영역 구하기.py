import sys
sys.setrecursionlimit(10**6)

m,n,k = map(int,input().split())

# 모눈종이 초기화 : 직사각형 영역은 False, 빈 곳은 True로
field = [[True]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            field[y][x] = False

# dfs 이동방향
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# dfs 함수
def dfs(x,y):
    field[x][y] = False
    area = 1
    for i in range(4):
        newx, newy = x+dx[i], y+dy[i]
        if 0 <= newx < m and 0 <= newy < n and field[newx][newy]:
            area += dfs(newx,newy)
    return area

# 정답 출력
answerlist = []
for i in range(m):
    for j in range(n):
        if field[i][j]:
            answerlist.append(dfs(i,j))
answerlist.sort()
print(len(answerlist))
print(*answerlist)