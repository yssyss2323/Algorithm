from collections import deque

class Belt:
    def __init__(self, state, k):
        self.state = deque(state)
        self.limit = k
        self.step = 0
        self.length = len(state) // 2
        self.disable = 0

    def rotation(self):
        self.state.rotate()
        self.state[self.length - 1][0] = False

    def robot_move(self):
        for i in range(self.length - 2, -1, -1):
            if self.state[i][0] and not self.state[i + 1][0] and self.state[i + 1][1] >= 1:
                self.state[i][0] = False
                self.state[i + 1][0] = True
                self.state[i + 1][1] -= 1
                if self.state[i + 1][1] == 0:
                    self.disable += 1

        if self.state[self.length - 1][0]:
            self.state[self.length - 1][0] = False

    def robot_upload(self):
        if self.state[0][1] > 0:
            self.state[0][0] = True
            self.state[0][1] -= 1
            if self.state[0][1] == 0:
                self.disable += 1

    def terminate_check(self):
        return self.disable >= self.limit


n, k = map(int, input().split())
durablity = list(map(int, input().split()))
state = [[False, d] for d in durablity]

belt = Belt(state, k)
while True:
    belt.step += 1
    belt.rotation()
    belt.robot_move()
    belt.robot_upload()
    if belt.terminate_check():
        print(belt.step)
        break
