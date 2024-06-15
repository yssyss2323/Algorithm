import sys

input = sys.stdin.readline
N, M = map(int, input().split())
DNAs = []
for _ in range(N):
    DNAs.append(input())

answer_DNA = ''
answer_sum = 0
for i in range(M):
    ACGT = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # [0, 0, 0, 0]
    for j in range(N):
        ACGT[DNAs[j][i]] += 1
    tmp_max = max(ACGT.values())
    for key in ACGT.keys():
        if ACGT.get(key) == tmp_max:
            answer_DNA += key
            break
    answer_sum += N - tmp_max

print(answer_DNA)
print(answer_sum)
