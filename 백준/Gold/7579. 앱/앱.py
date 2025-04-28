import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 가능한 최대 비용: 모든 앱을 껐을 때 비용 총합
max_cost = sum(cost)

# dp[i] = i 비용을 들였을 때 확보할 수 있는 최대 메모리
dp = [0] * (max_cost + 1)

# 앱 하나씩 고려
for i in range(N):
    m = memory[i]
    c = cost[i]
    # dp 갱신은 **큰 쪽부터** 해야 해 (같은 앱을 여러 번 쓰는 걸 방지하려고)
    for j in range(max_cost, c-1, -1):
        dp[j] = max(dp[j], dp[j-c] + m)

# 최소 비용 찾기
for i in range(max_cost + 1):
    if dp[i] >= M:
        print(i)
        break
