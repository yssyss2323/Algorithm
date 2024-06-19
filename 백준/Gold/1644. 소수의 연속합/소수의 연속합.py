n = int(input())
if n == 1:
    print(0)
else:
    prime = [False] * 2 + [True] * (n - 1)
    sum_of_primes = [0]
    for i in range(2, n + 1):
        if prime[i]:
            sum_of_primes.append(sum_of_primes[-1] + i)
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    m = len(sum_of_primes)
    answer = 0
    start, end = 0, 0
    while end < m:
        if end == m - 1 and sum_of_primes[end] - sum_of_primes[start] < n:
            break
        else:
            if sum_of_primes[end] - sum_of_primes[start] < n:
                end += 1
            elif sum_of_primes[end] - sum_of_primes[start] > n:
                start += 1
            else:
                answer += 1
                start += 1
                end += 1
    print(answer)