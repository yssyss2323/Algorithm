from collections import deque

def find_distance(arr, x):
    distance = 0
    while arr:
        target = arr.pop()
        for _ in range(x - 1):
            if arr:
                arr.pop()
        distance += target * 2
    return distance


n,m = map(int, input().split())
book_place = list(map(int, input().split()))
left, right = [0], [0]
for place in book_place:
    if place < 0:
        left.append(abs(place))
    else:
        right.append(place)
left.sort()
right.sort()
long_place = max(left[-1], right[-1])

ans = 0
ans += find_distance(left, m)
ans += find_distance(right, m)
ans -= long_place
print(ans)