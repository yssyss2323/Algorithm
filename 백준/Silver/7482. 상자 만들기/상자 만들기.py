import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    ans = float(input()) / 6
    print(f"{ans:.10f}")
