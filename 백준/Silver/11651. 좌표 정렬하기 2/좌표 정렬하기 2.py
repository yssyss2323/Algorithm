import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
coordinates = []
for _ in range(N):
    x, y = map(int,input().split())
    coordinates.append((y,x))
coordinates.sort()
for coordinate in coordinates:
    print(coordinate[1], coordinate[0])