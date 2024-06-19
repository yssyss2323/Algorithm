def mul_mat(A,B):
    C = []
    C.append([(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 1000000007, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 1000000007])
    C.append([(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 1000000007, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 1000000007])
    return C

def pow(A,n):
    for _ in range(n):
        A = mul_mat(A,A)
    return A

def fibo(n):
    x = bin(n)[2:]
    bin_power = []
    for i in range(len(x)):
        if x[i] == '1':
            bin_power.append(len(x) - i - 1)
    F = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    for i in bin_power:
        ans = mul_mat(ans, pow(F, i))
    return ans[1][0]


if __name__ == "__main__":
    n = int(input())
    ans = fibo(n + 1) * fibo(n) % 1000000007
    print(ans)
