# x까지 에라스토테네스의 체 적용 함수
def make_prime_list(x):
    if x <= 2:
        return [False] * x
    else:
        arr = [False] * 2 + [True] * (x - 1)
        for i in range(2, x + 1):
            if arr[i]:
                for j in range(i * 2, x + 1, i):
                    arr[j] = False
        return arr

# 4이상의 짝수를 두 소수로 분해하는 함수
def even_to_prime(x):
    check = make_prime_list(x)
    tmp = x // 2
    if tmp % 2 == 0 and tmp != 2:
        tmp += 1
    for i in range(tmp, x, 2):
        if check[i] and check[x - i]:
            return [x - i, i]

n = int(input())
if n < 8:
    print(-1)
else:
    if n % 2:
        answerlist = [2, 3] + even_to_prime(n - 5)
        print(*answerlist)
    else:
        answerlist = [2, 2] + even_to_prime(n - 4)
        print(*answerlist)
