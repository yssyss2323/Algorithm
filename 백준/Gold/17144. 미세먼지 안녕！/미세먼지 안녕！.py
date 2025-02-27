direct = [(0, 0), (0, -1), (1, 0), (-1, 0), (0, 1)]

def spread_dust(room, r, c):
    for i in range(r):
        for j in range(c):
            for k in range(1, 5):
                di = i + direct[k][0]
                dj = j + direct[k][1]
                cnt = 0
                if 0 <= di < r and 0 <= dj < c and room[i][j][0] != -1 and room[di][dj][0] != -1:
                    room[di][dj][2] += room[i][j][0] // 5
                    cnt += 1
                room[i][j][2] -= cnt * room[i][j][0] // 5
    for i in range(r):
        for j in range(c):
            room[i][j][0] += room[i][j][2]
            room[i][j][2] = 0

def cleaning(room, r, c):
    for i in range(r):
        for j in range(c):
            if room[i][j][0] != -1:
                direction = direct[room[i][j][1]]
                di = i + direction[0]
                dj = j + direction[1]
                room[di][dj][2] = room[i][j][0]
    for i in range(r):
        for j in range(c):
            if room[i][j][0] == -1:
                room[i][j][2] = 0
            else:
                room[i][j][0] = room[i][j][2]
                room[i][j][2] = 0


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
            tmp.append([row[j], 0, 0])
        room.append(tmp)
    for i in range(c):
        room[0][i][1] = 1
        room[r - 1][i][1] = 1
    for i in range(aircon[0][0]):
        room[i][0][1] = 2
    for i in range(1, aircon[0][0] + 1):
        room[i][c - 1][1] = 3
    for i in range(aircon[1][0] + 1, r):
        room[i][0][1] = 3
    for i in range(aircon[1][0], r - 1):
        room[i][c - 1][1] = 2
    for i in range(c - 1):
        room[aircon[0][0]][i][1] = 4
        room[aircon[1][0]][i][1] = 4

    for i in range(t):
        spread_dust(room, r, c)
        cleaning(room, r, c)

    ans = 2
    for i in range(r):
        for j in range(c):
            ans += room[i][j][0]
    print(ans)