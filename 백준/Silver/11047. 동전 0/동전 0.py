N, K = map(int, input().split())
A = []
for _ in range(N):
    cost = int(input())
    if cost <= K:
        A.append(cost)
answer = 0
for i in range(len(A) - 1, -1, -1):
    cost = A[i]
    answer += K // cost
    K %= cost
    if K == 0:
        break
print(answer)