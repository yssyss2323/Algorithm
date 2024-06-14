from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
q = deque([0] * w)
total_weight = 0

time = 0
for i in range(n):
    truck = trucks[i]
    while True:
        total_weight -= q[0]
        q[0] = 0
        q.rotate(-1)
        time += 1

        if total_weight + truck <= L:
            q[w - 1] = truck
            total_weight += truck
            break

print(time + w)
