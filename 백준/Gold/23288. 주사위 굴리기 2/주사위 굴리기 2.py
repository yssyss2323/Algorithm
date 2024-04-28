EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4

def check_direction(now_x, now_y, direction):
    check = {EAST: (now_y == m - 1),
             WEST: (now_y == 0),
             NORTH: (now_x == 0),
             SOUTH: (now_x == n - 1)}
    return check[direction]

def rotate(direction, angle):
    RIGHT_90 = {EAST: SOUTH, WEST: NORTH, NORTH: EAST, SOUTH: WEST}
    LEFT_90 = {EAST: NORTH, WEST: SOUTH, NORTH: WEST, SOUTH: EAST}
    REFLECTION = {EAST: WEST, WEST: EAST, NORTH: SOUTH, SOUTH: NORTH}
    check = {90: RIGHT_90, -90: LEFT_90, 180: REFLECTION}
    return check[angle][direction]

def update_direction(now_x, now_y, dice, given_map, direction):
    if dice[0] > given_map[now_x][now_y]:
        direction = rotate(direction, 90)
    elif dice[0] < given_map[now_x][now_y]:
        direction = rotate(direction, -90)
    if check_direction(now_x, now_y, direction):
        direction = rotate(direction, 180)
    return direction

def update_coordinate(now_x, now_y, direction):
    check = {EAST: (now_x, now_y + 1),
             WEST: (now_x, now_y - 1),
             NORTH: (now_x - 1, now_y),
             SOUTH: (now_x + 1, now_y)}
    return check[direction]

def move_dice(dice, direction):
    check = {EAST: [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]],
             WEST: [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]],
             NORTH: [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]],
             SOUTH: [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]}
    return check[direction]

def get_point(now_x, now_y, given_map):
    B = given_map[now_x][now_y]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[now_x][now_y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [[now_x, now_y]]
    C = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and given_map[next_x][next_y] == B:
                C += 1
                visited[next_x][next_y] = True
                stack.append([next_x, next_y])
    return B * C

n, m, k = map(int, input().split())
X, Y = 0, 0
my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().split())))
my_dice = [6, 3, 4, 2, 5, 1]
now_direction = EAST
if check_direction(X, Y, now_direction):
    now_direction = WEST

point = 0
for _ in range(k):
    X, Y = update_coordinate(X, Y, now_direction)
    my_dice = move_dice(my_dice, now_direction)
    point += get_point(X, Y, my_map)
    now_direction = update_direction(X, Y, my_dice, my_map, now_direction)
print(point)
