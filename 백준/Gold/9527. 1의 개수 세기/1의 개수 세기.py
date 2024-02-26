# n이하의 모든 이진수에 있는 1의 개수를 세는 함수
def countone(n):
    nn = bin(n)[2:]
    length = len(nn)
    checkone = 0 # 현재 자리수 기준 왼쪽의 1의 개수
    answer = 0
    for i in range(length - 1):
        if nn[i] == '1':
            tmp = length - i - 1 # 현재 자리수 기준 오른쪽의 자리수
            answer += checkone * 2 ** tmp + tmp * 2 ** (tmp - 1) + 1
            checkone += 1
    answer += (checkone + 1) * int(nn[length - 1]) # 맨 마지막 자리가 1인 경우
    return answer

a,b = map(int,input().split())
print(countone(b) - countone(a -1))