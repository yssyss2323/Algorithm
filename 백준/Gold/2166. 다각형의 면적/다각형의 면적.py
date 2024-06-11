import sys
input = sys.stdin.readline

N = int(input())
xpoints, ypoints = [], []
for _ in range(N):
    x, y = map(int, input().split())
    xpoints.append(x)
    ypoints.append(y)
xpoints.append(xpoints[0])
ypoints.append(ypoints[0])

answer = 0
for i in range(N):
    answer += (xpoints[i] * ypoints[i + 1]) - (ypoints[i] * xpoints[i + 1])
answer = abs(answer * 0.5)

if answer * 10 - int(answer * 10) < 0.5:
    answer = int(answer * 10) / 10
else:
    answer = int(answer * 10 + 1) / 10
print(answer)