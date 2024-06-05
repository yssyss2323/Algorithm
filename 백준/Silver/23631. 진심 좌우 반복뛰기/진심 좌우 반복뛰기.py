import sys
input = lambda: sys.stdin.readline().rstrip()

def distance(n, k):
    return k * n * (n + 1) // 2

def find_now(n, k):
    sign = 1
    if n % 2 == 0:
        sign = -1
    return sign * ((n + 1) // 2) * k

def direction_right(n):
    if n % 2 == 0:
        return 1
    else:
        return -1

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    i = int(((N - 1) * 2 / K) ** 0.5) - 1
    if distance(i + 1, K) < N - 1:
        i += 1
    now = find_now(i, K) + direction_right(i) * (N - 1 - distance(i, K))
    tmp_direction = direction_right(i)
    if distance(i + 1, K) == N - 1:
        tmp_direction *= -1
    direction = 'R' if tmp_direction == 1 else 'L'
    print(now, direction)
