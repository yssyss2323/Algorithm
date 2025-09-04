n = int(input())

like = [[] for _ in range(n ** 2 + 1)]
student_ord = []

for _ in range(n ** 2):
    tmp = list(map(int, input().split()))
    student = tmp[0]
    student_ord.append(student)
    like[student] = tmp[1:]

# 학생, 주변 빈자리 수, 인접 선호수
classroom = [[[0, 0, 0] for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i, j) in [(1, 1), (1, n), (n, 1), (n , n)]:
            classroom[i][j][1] = 2
        elif i in (1, n) or j in (1, n):
            classroom[i][j][1] = 3
        else:
            classroom[i][j][1] = 4

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check_cnt(student, x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if classroom[nx][ny][0] in like[student]:
            cnt += 1
    return cnt

def find_pos(student):
    pos = (0, 0)
    check = [-1, -1]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if classroom[i][j][0] > 0:
                continue
            cnt = check_cnt(student, i, j)
            if check[0] < cnt:
                check[0] = cnt
                check[1] = classroom[i][j][1]
                pos = (i, j)
            elif check[0] == cnt:
                if classroom[i][j][1] > check[1]:
                    check[1] = classroom[i][j][1]
                    pos = (i, j)
    classroom[pos[0]][pos[1]][0] = student
    for i in range(4):
        nx, ny = pos[0] + dx[i], pos[1] + dy[i]
        classroom[nx][ny][1] -= 1
        if classroom[nx][ny][0] in like[student]:
            classroom[pos[0]][pos[1]][2] += 1
        if student in like[classroom[nx][ny][0]]:
            classroom[nx][ny][2] += 1
    return pos

for student in student_ord:
    find_pos(student)

score = 0
score_board = [0, 1, 10, 100, 1000]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        score += score_board[classroom[i][j][2]]
print(score)