n = int(input())
fe = list(map(int, input().split()))
fe.sort()
sum = 0
for part in fe:
    sum += part
answer = 0
for part in fe:
    sum -= part
    answer += part * sum
print(answer)