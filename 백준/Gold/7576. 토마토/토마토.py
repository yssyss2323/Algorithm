from collections import deque
M,N = map(int,input().split())
# 맵 초기화
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))
newfield = [[-1]*(M+1)] + [[-1] + i + [-1] for i in field] + [[-1]*(M+1)]
# 익은 토마토 (큐)
welldone = deque()
for i in range(N+1):
    for j in range(M+1):
        if newfield[i][j] == 1:
            welldone.append([i,j,0])
# 이동방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]
day = 0
# bfs 수행
while welldone:
    x,y,z = welldone.popleft()
    for i in range(4):
        newx,newy = x+dx[i],y+dy[i]
        if newfield[newx][newy] == 0:
            welldone.append([newx,newy,z+1])
            newfield[newx][newy] = 1
            day = z+1
# 정답 출력
for row in newfield:
    if 0 in row:
        print(-1)
        break
else:
    print(day)