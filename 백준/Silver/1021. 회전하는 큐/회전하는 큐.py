N, M = map(int, input().split())
deq = [i for i in range(1, N + 1)]
wanted = list(map(int, input().split()))
answer = 0
for idx in wanted:
    now = deq.index(idx)
    left, right = deq[:now], deq[now + 1:]
    answer += min(len(left), len(right) + 1)
    deq = right + left
print(answer)