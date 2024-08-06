direction = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}

def sol(n, m, x, y):
    visited = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    visited[x][y][0] = True
    stack = [(x, y, 0)]
    while stack:
        curr_x, curr_y, curr_drc = stack.pop()
        next_drc = (curr_drc + 1) % 4
        next_x = curr_x + direction[curr_drc][0] * board[curr_x][curr_y]
        next_y = curr_y + direction[curr_drc][1] * board[curr_x][curr_y]
        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y][next_drc]:
                visited[next_x][next_y][next_drc] = True
                stack.append((next_x,next_y,next_drc))
            else:
                return True
        else:
            return False

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
arr = []
for i in range(n):
    if sol(n, m, i, 0):
        ans += 1
        arr.append(i + 1)
print(ans)
print(*arr)