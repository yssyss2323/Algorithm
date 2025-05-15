import sys
input = sys.stdin.readline

n = int(input())
height = 0
while 2 ** height < n:
    height += 1
seg = [float('inf') for _ in range(2 ** (height + 1))]
alist = list(map(int, input().split()))
for i in range(2 ** height):
    seg[2 ** height + i] = i
alist += [float('inf')] * (2 ** height - n)

for i in range(height):
    for j in range(2 ** (height - i), 2 ** (height - i + 1), 2):
        if alist[seg[j]] <= alist[seg[j + 1]]:
            seg[j // 2] = seg[j]
        else:
            seg[j // 2] = seg[j + 1]

for _ in range(int(input())):
    order, i, x = map(int, input().split())
    if order == 1:
        alist[i - 1] = x
        tmp = i + 2 ** height - 1
        tmp //= 2
        while tmp > 0:
            seg[tmp] = seg[tmp * 2] if alist[seg[tmp * 2]] <= alist[seg[tmp * 2 + 1]] else seg[tmp * 2 + 1]
            tmp //= 2
    else:
        start, end = i + 2 ** height - 1, x + 2 ** height - 1
        min_val = float('inf')
        ans = -1
        while start <= end:
            if start % 2 == 1:
                if min_val > alist[seg[start]]:
                    min_val = alist[seg[start]]
                    ans = seg[start]
                elif min_val == alist[seg[start]]:
                    if ans > seg[start]:
                        ans = seg[start]
            if end % 2 == 0:
                if min_val > alist[seg[end]]:
                    min_val = alist[seg[end]]
                    ans = seg[end]
                elif min_val == alist[seg[end]]:
                    if ans > seg[end]:
                        ans = seg[end]
            start = (start + 1) // 2
            end = (end - 1) // 2
        print(ans + 1)