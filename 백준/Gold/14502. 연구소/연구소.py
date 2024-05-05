class LabSimulation:
    def __init__(self, N, M, lab_data):
        self.N = N
        self.M = M
        self.lab = lab_data
        self.my_space = []
        self.my_virus = []
        for i in range(N):
            for j in range(M):
                if lab_data[i][j] == 0:
                    self.my_space.append((i, j))
                elif lab_data[i][j] == 2:
                    self.my_virus.append((i, j))

    def select_three(self):
        def C(x, y):
            if y == 1:
                return [[i] for i in range(x)]
            elif y == x:
                return [list(range(x))]
            else:
                tmp = [i + [x - 1] for i in C(x - 1, y - 1)] + C(x - 1, y)
                tmp.sort()
                return tmp
        selected = []
        for a, b, c in C(len(self.my_space), 3):
            selected.append((self.my_space[a], self.my_space[b], self.my_space[c]))
        return selected

    def make_wall(self, three_coordinates):
        for coordinate in three_coordinates:
            x, y = coordinate
            self.lab[x][y] = 1

    def break_wall(self, three_coordinates):
        for coordinate in three_coordinates:
            x, y = coordinate
            self.lab[x][y] = 0

    def dfs(self):
        virtual_lab = [row[:] for row in self.lab]
        virtual_virus = self.my_virus[:]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while virtual_virus:
            x, y = virtual_virus.pop()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < self.N and 0 <= ny < self.M and virtual_lab[nx][ny] == 0:
                    virtual_virus.append((nx, ny))
                    virtual_lab[nx][ny] = 2
        return virtual_lab

    def counting_safe_place(self, lab):
        cnt = 0
        for i in range(self.N):
            for j in range(self.M):
                if lab[i][j] == 0:
                    cnt += 1
        return cnt

    def solution(self):
        answer = -float('inf')
        for crds in self.select_three():
            self.make_wall(crds)
            tmp = self.counting_safe_place(self.dfs())
            answer = max(tmp, answer)
            self.break_wall(crds)
        print(answer)


if __name__ == "__main__":
    N, M = map(int, input().split())
    lab_data = [list(map(int, input().split())) for _ in range(N)]
    simulation = LabSimulation(N, M, lab_data)
    simulation.solution()
