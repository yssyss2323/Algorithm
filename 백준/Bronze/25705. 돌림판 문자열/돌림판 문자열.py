from collections import deque

n = int(input())
mater = deque(input())
m = int(input())
goal = input()

ans = 0
for i in range(m):
    curr = goal[i]
    try:
        idx = mater.index(curr)
    except:
        print(-1)
        break
    ans += idx + 1
    mater.rotate(-1 - idx)
else:
    print(ans)