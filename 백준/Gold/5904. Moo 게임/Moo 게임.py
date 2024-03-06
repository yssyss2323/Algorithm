# 문자열 S(x)에서 n번째 글자를 구하는 함수
def f(x, n):
    if x == 3:
        return 'm' if n == 1 else 'o'
    else: # x > 3일때
        if 2 ** (x - 1) - (x + 1) < n < 2 ** (x - 1):
            return 'm' if n == 2 ** (x - 1) - x else 'o'
        else:
            if n >= 2 ** (x - 1):
                n -= 2 ** (x - 1) - 1
            return f(x - 1, n)

N = int(input())
X = 3
while 2 ** X - (X + 2) < N:
    X += 1
print(f(X, N))
