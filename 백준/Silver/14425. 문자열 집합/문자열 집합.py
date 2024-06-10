import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set() # 시간복잡도 충족을 위해 리스트 대신 탐색 O(1)인 set사용
for _ in range(N):
    S.add(input())

cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1
print(cnt)
