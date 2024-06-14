from collections import deque, defaultdict
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
q = deque()
length_dic = defaultdict(int) # 앞선 제출코드가 왠지모르게 키에러 떠서 디폴트딕 사용했음

answer = 0
# step 1 : q에 k + 1개의 원소를 채운다
dum = 1 if K < N else 0 # 문제 조건상 빈틈이 있어서 할 수 없이 잡기술 사용
for _ in range(K + dum):
    name_length = len(input())
    answer += length_dic[name_length] # count 사용시 시간초과 예상 -> 딕셔너리 사용
    length_dic[name_length] += 1 # 이름길이 카운팅 현황 업데이트
    q.append(name_length)

# step 2 : 나머지 원소들을 차례로 넣어주면서 동시에 앞원소들을 배출
for _ in range(N - K - 1):
    length_dic[q[0]] -= 1 # 앞원소 제거 및 이름길이 카운팅 현황 업데이트
    q[0] = 0
    q.rotate(-1)
    name_length = len(input())
    answer += length_dic[name_length]
    length_dic[name_length] += 1
    q[K] = name_length

print(answer)
