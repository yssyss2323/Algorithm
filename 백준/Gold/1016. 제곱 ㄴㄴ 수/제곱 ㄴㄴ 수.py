min_num, max_num = map(int,input().split())

end = int(max_num ** 0.5) + 1
prime = [False] * 2 + [True] * end
square_num = []
for i in range(2, end + 1):
    if prime[i]:
        square_num.append(i ** 2)
        for j in range(i * 2, end + 1, i):
            prime[j] = False

total = max_num - min_num + 1
check = [True] * total
for i in square_num:
    x = (min_num // i + 1) * i - min_num  if min_num % i else 0
    for j in range(x, total, i):
        check[j] = False

answer = 0
for i in check:
    if i:
        answer += 1
print(answer)