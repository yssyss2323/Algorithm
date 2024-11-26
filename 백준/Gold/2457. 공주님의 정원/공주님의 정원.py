import sys
input = sys.stdin.readline

n = int(input())

arr = []
start = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x, y = 100 * a + b, 100 * c + d
    if x <= 301:
        if y > start:
            start = y
    else:
        arr.append((x, y))
arr.sort()
arr.append((9999, 9999))

if start <= 301:
    print(0)
elif start > 1130:
    print(1)
else:
    ans = 1
    tmp = 0
    for day in arr:
        if day[0] <= start:
            if day[1] > tmp:
                tmp = day[1]
        else:
            if day[0] != 9999 and day[0] > tmp:
                print(0)
                break
            ans += 1
            if tmp > 1130:
                print(ans)
                break
            start = tmp
            tmp = day[1]
    else:
        print(0)