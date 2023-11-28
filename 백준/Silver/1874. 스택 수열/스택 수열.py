import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tmp= 1
arr = []
answer = ''
for _ in range(n):
    num = int(input())
    while tmp <= num:
        arr.append(tmp)
        answer += '+'
        tmp += 1
    if num == arr[-1]:
        arr.pop()
        answer += '-'
    else:
        print("NO")
        break
else:
    for ii in answer:
        print(ii)