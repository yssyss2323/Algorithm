import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
words = [input() for _ in range(n)]

# 길이 m의 단어를 길이 1 ~ 길이 m으로 잘라서 딕셔너리에 넣어 카운팅 -> 최대 O(2000000)
check = dict()
for word in words:
    tmp = ''
    for ch in word:
        tmp += ch
        check[tmp] = check.get(tmp,0) + 1

# 가장 긴 접두사 shared와 그 길이 max_length 구하기
shared, max_length = '', 0
for a,b in check.items():
    tmp_length = len(a)
    if b > 1:
        if tmp_length > max_length:
            shared = a
            max_length = tmp_length

# 접두사 공유하는 가장 앞쪽의 단어 탐색
cnt = 0
for word in words:
    if shared == word[:max_length]:
        cnt += 1
        print(word)
    if cnt == 2:
        break
