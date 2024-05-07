NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

class RobotSimulation:
    def __init__(self, N, M, r, c, direction, place):
        self.N = N
        self.M = M
        self.r = r
        self.c = c
        self.num_cleaned = 0
        self.direction = direction
        self.move = {NORTH:(-1,0), EAST:(0,1), SOUTH:(1,0), WEST:(0,-1)}
        self.move_back = {NORTH:(1,0), EAST:(0,-1), SOUTH:(-1,0), WEST:(0,1)}
        self.rotate = {NORTH:WEST, EAST:NORTH, SOUTH:EAST, WEST:SOUTH}
        self.place = place
        self.visited = [row[:] for row in place]
        '''for i in range(N):
            for j in range(M):
                if place[i][j] == 0:
                    self.visited[i][j] = False'''

    def clean(self):
        if not self.visited[self.r][self.c]:
            self.num_cleaned += 1
            self.visited[self.r][self.c] = self.num_cleaned

    def check_clean_around(self):
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = self.r + dr, self.c + dc
            if self.place[nr][nc] == 0 and not self.visited[nr][nc]:
                return False
        return True

    def move_case1(self):
        nr = self.r + self.move_back[self.direction][0]
        nc = self.c + self.move_back[self.direction][1]
        if self.place[nr][nc] == 0:
            self.r, self.c = nr, nc
            return False
        else:
            return True

    def move_case2(self):
        for _ in range(4):
            self.direction = self.rotate[self.direction]
            nr, nc = self.r + self.move[self.direction][0], self.c + self.move[self.direction][1]
            if self.place[nr][nc] == 0 and not self.visited[nr][nc]:
                self.r, self.c = nr, nc
                break

    def simulation(self):
        is_end = False
        while not is_end:
            self.clean()
            if self.check_clean_around():
                is_end = self.move_case1()
            else:
                self.move_case2()
        return self.num_cleaned


if __name__ == "__main__":
    N, M = map(int,input().split())
    r, c, d = map(int,input().split())
    my_place = []
    for _ in range(N):
        my_place.append(list(map(int,input().split())))
    my_robot = RobotSimulation(N,M,r,c,d,my_place)
    print(my_robot.simulation())
