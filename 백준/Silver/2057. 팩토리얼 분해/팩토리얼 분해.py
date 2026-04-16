def factorial(n):
    val = 1
    for i in range(2, n + 1):
        val *= i
    return val


n = int(input())
candidate = set([0])
i = 0
while True:
    curr = factorial(i)
    if curr > n:
        break
    tmp = set()
    for num in candidate:
        tmp.add(num + curr)
    candidate = candidate.union(tmp)
    i += 1
candidate.remove(0)

print('YES' if n in candidate else 'NO')