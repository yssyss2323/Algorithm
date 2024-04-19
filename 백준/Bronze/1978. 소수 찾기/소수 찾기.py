N = int(input())
num = list(map(int,input().split()))

prime = [False] * 2 + [True] * 1000
for i in range(1001):
    if prime[i]:
        for j in range(i*2,1001,i):
            prime[j] = False

answer = 0
for i in num:
    if prime[i]:
        answer += 1
print(answer)