def find_pair(N):  # 합이 N이 되는 서로소인 두 수의 쌍의 개수
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    cnt = 0
    for i in range(1, N // 2 + 1):
        if gcd(i, N - i) == 1:
            cnt += 1
    return cnt

def factorization(N):
    factor = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            factor.append(i)
            factor.append(N // i)
    if int(N ** 0.5) == N ** 0.5:
        factor.pop()
    return factor

def solution(N):
    answer = 0
    for i in factorization(N):
        answer += find_pair(N // i + 1)
    return answer


print(solution(int(input())))
