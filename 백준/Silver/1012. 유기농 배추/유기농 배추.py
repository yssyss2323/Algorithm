import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1

    ans = 0
    stack = []
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                field[i][j] = 2 # 방문처리
                ans += 1
                stack.append([i,j])
                while stack:
                    now_x, now_y = stack.pop()
                    for k in range(4):
                        next_x = now_x + dx[k]
                        next_y = now_y + dy[k]
                        if 0 <= next_x < M and 0 <= next_y < N:
                            if field[next_x][next_y] == 1:
                                field[next_x][next_y] = 2
                                stack.append([next_x,next_y])
    print(ans)
