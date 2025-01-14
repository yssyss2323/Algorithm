from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def find_target(room, shark_size, shark_pos):
    targets = []
    q = deque([[shark_pos, 0]])
    d = float('inf')
    visited = [[False for _ in range(len(room[0]))] for _ in range(len(room))]
    visited[shark_pos[0]][shark_pos[1]] = True
    while q:
        curr, dist = q.popleft()
        if 0 < room[curr[0]][curr[1]] < shark_size:
            if d >= dist:
                d = dist
                targets.append([curr[0], curr[1], dist])
        for k in range(4):
            next_x = curr[0] + dx[k]
            next_y = curr[1] + dy[k]
            if 0 <= next_x < len(room) and 0 <= next_y < len(room[0]) and not visited[next_x][next_y]:
                if room[next_x][next_y] <= shark_size and d > dist:
                    q.append([[next_x, next_y], dist + 1])
                    visited[next_x][next_y] = True
    return targets


def solve():
    n = int(input())
    room = []
    shark_size = [2, 0]
    curr_pos = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        if 9 in tmp:
            j = tmp.index(9)
            tmp[j] = 0
            curr_pos = [i, j]
        room.append(tmp)

    time = 0
    while True:
        targets = find_target(room, shark_size[0], curr_pos)
        # print('-' * 10, time, shark_size, target)
        # for row in room:
        #     print(*row)

        # print(target)
        if not targets:
            print(time)
            break
        else:
            targets.sort(key=lambda x: [x[2], x[0], x[1]])
            target = targets[0]
            time += target[2]
            shark_size[1] += 1
            if shark_size[0] == shark_size[1]:
                shark_size[0] += 1
                shark_size[1] = 0
            curr_pos = [target[0], target[1]]
            room[target[0]][target[1]] = 0


if __name__ == "__main__":
    solve()
