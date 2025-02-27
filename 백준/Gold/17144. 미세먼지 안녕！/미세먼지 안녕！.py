direct = [(0, -1), (1, 0), (-1, 0), (0, 1)]

def spread_dust(room, r, c):
    for i in range(r):
        for j in range(c):
            for k in range(4):
                di = i + direct[k][0]
                dj = j + direct[k][1]
                cnt = 0
                if 0 <= di < r and 0 <= dj < c and room[i][j][0] != -1 and room[di][dj][0] != -1:
                    room[di][dj][1] += room[i][j][0] // 5
                    cnt += 1
                room[i][j][1] -= cnt * room[i][j][0] // 5
    for i in range(r):
        for j in range(c):
            room[i][j][0] += room[i][j][1]
            room[i][j][1] = 0

def cleaning(room, r, c):
    for xx in range(2):
        machine = aircon[xx]
        for i in range(c - 1):
            if i != machine[1]:
                room[machine[0]][i + 1][1] = room[machine[0]][i][0]

        if xx == 0:
            for i in range(machine[0], 0, -1):
                if machine[1] != c - 1:
                    room[i - 1][c - 1][1] = room[i][c - 1][0]
            for i in range(machine[0]):
                room[i + 1][0][1] = room[i][0][0]
        else:
            for i in range(machine[0], r - 1):
                if machine[1] != c - 1:
                    room[i + 1][c - 1][1] = room[i][c - 1][0]
            for i in range(r - 1, machine[0], -1):
                room[i - 1][0][1] = room[i][0][0]

    for i in range(1, c):
        room[0][i - 1][1] = room[0][i][0]
        room[r - 1][i - 1][1] = room[r - 1][i][0]

    for i in range(c):
        room[0][i][0] = room[0][i][1]
        room[0][i][1] = 0

        room[r - 1][i][0] = room[r - 1][i][1]
        room[r - 1][i][1] = 0

    for i in range(1, r - 1):
        room[i][0][0] = room[i][0][1]
        room[i][0][1] = 0

        room[i][c - 1][0] = room[i][c - 1][1]
        room[i][c - 1][1] = 0

    for xx in range(2):
        machine = aircon[xx]
        for i in range(1, c - 1):
            room[machine[0]][i][0] = room[machine[0]][i][1]
            room[machine[0]][i][1] = 0

        room[machine[0]][machine[1]] = [-1, 0]



if __name__ == "__main__":
    r, c, t = map(int, input().split())
    room = []
    aircon = []
    for i in range(r):
        row = list(map(int, input().split()))
        tmp = []
        for j in range(c):
            if row[j] == -1:
                aircon.append((i, j))
            tmp.append([row[j], 0])
        room.append(tmp)

    for i in range(t):
        spread_dust(room, r, c)
        cleaning(room, r, c)

    ans = 2
    for i in range(r):
        for j in range(c):
            ans += room[i][j][0]
    print(ans)