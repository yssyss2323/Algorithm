from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


r, c = map(int, input().split())

# 맵초기화 : '!'으로 패딩
field = [['!'] * (c + 2)]
for _ in range(r):
    field.append(['!'] + list(input())+ ['!'])
field.append(['!'] * (c + 2))

# 불, 사람 각각 큐 구현 / 처음좌표 찾기
fire, human = deque(), deque()
for i in range(r+2):
    for j in range(c+2):
        if field[i][j] == 'F':
            fire.append([i, j])
        if field[i][j] == 'J':
            human.append([i, j, 0])

# 이동방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs 수행
answer = False
while human:
    # 불 확산
    tmp = deque()
    while fire:
        xfire, yfire = fire.popleft()
        for i in range(4):
            nxfire, nyfire = xfire + dx[i], yfire + dy[i]
            if field[nxfire][nyfire] in '.J': # 불이 확산가능한 곳
                tmp.append([nxfire, nyfire])
                field[nxfire][nyfire] = 'F' # 불 확산된 곳 갱신
    fire = tmp
    # 사람 이동방향 탐색
    tmp2 = deque()
    while human:
        xman, yman, tman = human.popleft()
        for i in range(4):
            nxman, nyman, ntman = xman + dx[i], yman + dy[i], tman + 1
            if field[nxman][nyman] == '!': # 탈출성공
                answer = ntman
            if field[nxman][nyman] == '.':
                tmp2.append([nxman,nyman,ntman])
                field[nxman][nyman] = 'J' # 사람이 이동한 곳 갱신
    human = tmp2
    # while문 탈출조건
    if answer:
        print(answer)
        break
else:
    print('IMPOSSIBLE')