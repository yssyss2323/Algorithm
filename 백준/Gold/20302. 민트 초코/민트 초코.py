import sys
input = lambda: sys.stdin.readline().rstrip()

# mul은 곱하는 정수, div는 나누는 정수
mul, div = [], []
n = int(input())
expression = list(('* ' + input()).split())
for i in range(0, len(expression), 2):
    if expression[i] == '*':
        tmp = expression[i + 1]
        if tmp == '0':
            print("mint chocolate")
            exit()
        mul.append(abs(int(tmp)))
    else:
        div.append(abs(int(expression[i + 1])))

# factors는 소인수 개수 세는 딕셔너리
factors = {}
# 소인수분해하는 함수 : case는 곱하는 정수일때 1, 나누는 정수일때 -1
def decomp(x, case):
    i = 2
    while i ** 2 <= x:
        if x % i:
            i += 1
        else:
            x //= i
            if i in factors.keys():
                factors[i] += 1 * case
            else:
                factors[i] = 1 * case
    if x > 1:
        if x in factors.keys():
            factors[x] += 1 * case
        else:
            factors[x] = 1 * case
    return

for i in mul:
    decomp(i, 1)
for i in div:
    decomp(i, -1)

# 정답 출력
for i in factors.values():
    if i < 0:
        print("toothpaste")
        break
else:
    print("mint chocolate")