def select_three(space):
    def C(x,y):
        if y == 1:
            return [[i] for i in range(x)]
        elif y == x:
            return [list(range(x))]
        else:
            tmp = [i + [x-1] for i in C(x-1,y-1)] + C(x-1,y)
            tmp.sort()
            return tmp
    selected = []
    for a,b,c in C(len(space),3):
        selected.append((space[a], space[b], space[c]))
    return selected

def make_wall(lab,three_coordinates):
    for coordinate in three_coordinates:
        x,y = coordinate
        lab[x][y] = 1
    return lab

def break_wall(lab, three_coordinates):
    for coordinate in three_coordinates:
        x,y = coordinate
        lab[x][y] = 0
    return lab

def dfs(lab, virus):
    virtual_lab = [row[:] for row in lab]
    virtual_virus = virus[:]
    while virtual_virus:
        x,y = virtual_virus.pop()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(virtual_lab) and 0 <= ny < len(virtual_lab[0]) and virtual_lab[nx][ny] == 0:
                virtual_virus.append((nx,ny))
                virtual_lab[nx][ny] = 2
    return virtual_lab

def counting_safe_place(lab):
    cnt = 0
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 0:
                cnt += 1
    return cnt

def solution():
    N ,M = map(int,input().split())
    my_lab = []
    my_space = []
    my_virus = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        for j in range(M):
            if tmp[j] == 0:
                my_space.append((i,j))
            if tmp[j] == 2:
                my_virus.append((i,j))
        my_lab.append(tmp)

    answer = -float('inf')
    for crds in select_three(my_space):
        make_wall(my_lab,crds)
        tmp = counting_safe_place(dfs(my_lab,my_virus))
        answer = max(tmp,answer)
        break_wall(my_lab, crds)
    print(answer)

solution()
