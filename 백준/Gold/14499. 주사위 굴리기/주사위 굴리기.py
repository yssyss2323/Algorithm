def check_order(now_x, now_y, direction):
    if direction == 1:
        return False if now_y == m - 1 else True
    elif direction == 2:
        return False if now_y == 0 else True
    elif direction == 3:
        return False if now_x == 0 else True
    else:
        return False if now_x == n - 1 else True

def update_coordinate(now_x, now_y, direction):
    if direction == 1:
        next_x, next_y = now_x, now_y + 1
    elif direction == 2:
        next_x, next_y = now_x, now_y - 1
    elif direction == 3:
        next_x, next_y = now_x - 1, now_y
    else:
        next_x, next_y = now_x + 1, now_y
    return next_x, next_y

def move_dice(dice, direction):
    if direction == 1:
        dice = [dice[1],dice[5],dice[0],dice[3],dice[4],dice[2]]
    elif direction == 2:
        dice = [dice[2],dice[0],dice[5],dice[3],dice[4],dice[1]]
    elif direction == 3:
        dice = [dice[3],dice[1],dice[2],dice[5],dice[0],dice[4]]
    else:
        dice = [dice[4],dice[1],dice[2],dice[0],dice[5],dice[3]]
    return dice

def update_state(now_x,now_y,dice):
    if number_map[now_x][now_y]:
        dice[0] = number_map[now_x][now_y]
        number_map[now_x][now_y] = 0
    else:
        number_map[now_x][now_y] = dice[0]

n,m,x,y,k = map(int,input().split())
number_map = []
for _ in range(n):
    number_map.append(list(map(int,input().split())))
orders = list(map(int,input().split()))

my_dice = [0,0,0,0,0,0]
for order in orders:
    if check_order(x, y, order):
        x, y = update_coordinate(x, y, order)
        my_dice = move_dice(my_dice, order)
        update_state(x, y, my_dice)
        print(my_dice[5])
    else:
        continue