def dec_to_bin(n):
    tmp = bin(n)[2:]
    arr = []
    for i in range(len(tmp)):
        if tmp[i] == '1':
            arr.append(len(tmp) - i - 1)
    return arr

def mul_mat(mat1, mat2):
    mod = 10 ** 9
    a11 = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    a12 = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    a21 = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    a22 = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
    return [[a11 % mod, a12 % mod], [a21 % mod, a22 % mod]]

def pow_mat(mat, n):
    for _ in range(n):
        mat = mul_mat(mat, mat)
    return mat

def fibo(n):
    mat = [[1, 1], [1, 0]]
    nlist = dec_to_bin(n - 1)
    tmp = [[1, 0], [0, 1]]
    for i in nlist:
        tmp = mul_mat(pow_mat(mat, i), tmp)
    return tmp[0][0]


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        x = int(input())
        print(fibo(x))
