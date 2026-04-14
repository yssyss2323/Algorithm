n = int(input())
picture = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

norm_visited = [[False] * n for _ in range(n)]
jaejun_visited = [[False] * n for _ in range(n)]

def dfs(graph, visited, is_norm=True):
    length = len(graph)

    cnt = 0
    for i in range(length):
        for j in range(length):
            if not visited[i][j]:
                if is_norm or graph[i][j] == 'B':
                    curr_color = [graph[i][j]] # 일반탐색 또는 색맹탐색 중 파란색 탐색
                else:
                    curr_color = ['R', 'G'] # 색약탐색 중 빨간색 또는 초록색 탐색
                cnt += 1
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    curr_x, curr_y = stack.pop()
                    for k in range(4):
                        nx = curr_x + dx[k]
                        ny = curr_y + dy[k]
                        if 0 <= nx < length and 0 <= ny < length and not visited[nx][ny]:
                            if graph[nx][ny] in curr_color:
                                stack.append((nx, ny))
                                visited[nx][ny] = True
    return cnt

norm_cnt = dfs(picture, norm_visited)
jaejun_cnt = dfs(picture, jaejun_visited, False)
print(norm_cnt, jaejun_cnt)