x, y = map(int, input().split())
root = int(((x + y) * 2) ** 0.5)
if root * (root + 1) != (x + y) * 2:
    print(-1)
else:
    if x == 0:
        print(0)
    else:
        tmp = root
        ans = 1
        while x > tmp:
            ans += 1
            x -= tmp
            tmp -= 1
        print(ans)