import sys
input = lambda: sys.stdin.readline().rstrip()

def half_up(x):
    if x - int(x) < 0.5:
        return int(x)
    else:
        return int(x) + 1

n = int(input())
if n:
    opinions = []
    for _ in range(n):
        opinions.append(int(input()))

    start = half_up(n * 0.15)
    end = - start if start else n
    opinions.sort()
    answer = half_up(sum(opinions[start:end]) / (n - start * 2))
    print(answer)
else:
    print(0)
