# 최대공약수 함수
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# A*B 함수
def mat_mul(A, B):
    c00 = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 1000000007
    c01 = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 1000000007
    c10 = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 1000000007
    c11 = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 1000000007
    return [[c00, c01], [c10, c11]]

# A^(2^n) 함수
def mat_pow(A, n):
    for _ in range(n):
        A = mat_mul(A, A)
    return A

# 10진법 -> 2진법의 합 변환 함수
def sum_of_bin(x):
    tmp = bin(x)[2:]
    arr = []
    for i in range(len(tmp)):
        if tmp[i] == '1':
            arr.append(len(tmp) - i - 1)
    return arr

n, m = map(int, input().split())
Fibo = [[1, 1], [1, 0]]
ans = [[1, 0], [0, 1]]
target = sum_of_bin(gcd(n, m))
for i in target:
    ans = mat_mul(ans, mat_pow(Fibo, i))
print(ans[1][0])
