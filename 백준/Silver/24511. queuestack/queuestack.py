N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = []  # 주어진 큐스택에서 모든 큐를 합친 하나의 자료구조
for i in range(N):
    if A[i] == 0:  # 큐에 해당하는 경우
        q.append(B[i])
q.reverse()
if len(q) < M:
    q += C[:M - len(q)]
else:
    q = q[:M]
print(*q)
