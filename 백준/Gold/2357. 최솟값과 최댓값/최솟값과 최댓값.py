import sys
input = sys.stdin.readline

n, m = map(int, input().split())

size = 0
while 2 ** size < n:
    size += 1

seg_min = [float('inf') for _ in range(2 ** (size + 1))]
seg_max = [-float('inf') for _ in range(2 ** (size + 1))]

for i in range(n):
    tmp = int(input())
    seg_min[2 ** size + i] = tmp
    seg_max[2 ** size + i] = tmp

for i in range(size):
    for j in range(2 ** (size - i - 1), 2 ** (size - i)):
        seg_min[j] = min(seg_min[2 * j], seg_min[2 * j + 1])
        seg_max[j] = max(seg_max[2 * j], seg_max[2 * j + 1])

for _ in range(m):
    a, b = map(int, input().split())

    start = 2 ** size + a - 1
    end = 2 ** size + b - 1

    ans_min = float('inf')
    ans_max = -float('inf')

    while start <= end:
        if start % 2 == 1:
            ans_min = min(ans_min, seg_min[start])
            ans_max = max(ans_max, seg_max[start])
        if end % 2 == 0:
            ans_min = min(ans_min, seg_min[end])
            ans_max = max(ans_max, seg_max[end])
        start = (start + 1) // 2
        end = (end - 1) // 2
    print(ans_min, ans_max)
