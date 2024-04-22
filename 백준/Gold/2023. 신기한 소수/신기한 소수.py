def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

n = int(input())
now_prime = [2, 3, 5, 7]
for _ in range(n - 1):
    tmp = []
    for i in now_prime:
        for j in [1, 3, 7, 9]:
            test_num = i * 10 + j
            if is_prime(test_num):
                tmp.append(test_num)
    now_prime = tmp

for prime in now_prime:
    print(prime)
