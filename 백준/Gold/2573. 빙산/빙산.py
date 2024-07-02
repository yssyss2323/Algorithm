dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def after_melting(world, ices):
    arr = set()
    new_world = [[x for x in row] for row in world]
    sample = (-1, -1)
    for ice in ices:
        i, j = ice
        for t in range(4):
            if world[i + dx[t]][j + dy[t]] == 0 and new_world[i][j] >= 1:
                new_world[i][j] -= 1
        #print(world, new_world)
        if new_world[i][j] > 0:
            arr.add((i,j))
            sample = (i, j)
    return new_world, arr, sample


def dfs(world, arr, ice):
    stack = [ice]
    visited = set()
    while stack:
        now_x, now_y = stack.pop()
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if world[next_x][next_y] > 0 and (next_x, next_y) not in visited:
                stack.append((next_x, next_y))
                visited.add((next_x, next_y))
    if arr.difference(visited):
        return True
    else:
        return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    my_world = []
    ice_mountain = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(m):
            if tmp[j] > 0:
                ice_mountain.append((i, j))
        my_world.append(tmp)
    year = 0
    while True:
        my_world, arr, sample_ice = after_melting(my_world, ice_mountain)
        year += 1
        #print(sample_ice)
        #print(my_world)
        if sample_ice == (-1, -1):
            print(0)
            break
        else:
            if dfs(my_world, arr, sample_ice):
                print(year)
                break

