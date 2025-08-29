from collections import deque


def is_adjacent(str_num1, str_num2):
    cnt = 0
    for i in range(len(str_num1)):
        if str_num1[i] == str_num2[i]:
            cnt += 1
    return True if cnt == 3 else False

primes = [False] * 2 + [True] * 9999
check = []
for i in range(2, 10000):
    if primes[i]:
        if i > 1000:
            check.append(str(i))
        for j in range(i * 2, 10000, i):
            primes[j] = False

check_dict = {str_num:[] for str_num in check}
for i in range(len(check) - 1):
    num1 = check[i]
    for j in range(i + 1, len(check)):
        num2 = check[j]
        if is_adjacent(num1, num2):
            check_dict[num1].append(num2)
            check_dict[num2].append(num1)

def bfs(num1, num2):
    q = deque([(num1, 0)])
    visited = set()
    while q:
        curr, cnt = q.popleft()
        if curr == num2:
            print(cnt)
            break
        else:
            for num in check_dict[curr]:
                if num not in visited:
                    q.append((num, cnt + 1))
                    visited.add(num)
    else:
        print("Impossible")

for _ in range(int(input())):
    prime1, prime2 = input().split()
    bfs(prime1, prime2)