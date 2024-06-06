import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum_numbers = [0]
tmp = 0
for num in numbers:
    tmp += num
    sum_numbers.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_numbers[j] - sum_numbers[i - 1])
