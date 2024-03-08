k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

def cnt(x):
    sum = 0
    for line in lines:
        sum += line // x
    return sum

start, end = 1, max(lines)
while start <= end:
    mid = (start + end) // 2
    if cnt(mid) < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)