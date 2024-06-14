from collections import deque, defaultdict
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
q = deque()
length_dic = defaultdict(int)

answer = 0
for _ in range(K + 1):
    name_length = len(input())
    answer += length_dic[name_length]
    length_dic[name_length] += 1
    q.append(name_length)
for _ in range(N - K - 1):
    length_dic[q[0]] -= 1
    q[0] = 0
    q.rotate(-1)
    name_length = len(input())
    answer += length_dic[name_length]
    length_dic[name_length] += 1
    q[K] = name_length

print(answer)
