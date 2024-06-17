from collections import deque

n = int(input())
balloons = deque(map(int, input().split()))
nums = deque(range(1, n + 1))
while balloons:
    num = nums.popleft()
    print(num, end=' ')
    next = balloons.popleft()
    if next > 0:
        next = - next + 1
    else:
        next = - next
    nums.rotate(next)
    balloons.rotate(next)
