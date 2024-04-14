# A*B 함수
def mat_mul(A, B):
    c00 = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 10000
    c01 = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 10000
    c10 = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 10000
    c11 = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 10000
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

while True:
    Fibo = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    n = int(input())
    if n == -1:
        break
    else:
        target = sum_of_bin(n)
        for i in target:
            ans = mat_mul(ans, mat_pow(Fibo, i))
        print(ans[1][0])
