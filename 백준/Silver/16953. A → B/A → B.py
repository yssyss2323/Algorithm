A, B = map(int,input().split())
answer = 1
while B > A:
    if B % 10 == 1:
        B //= 10
        answer += 1
    elif B % 10 in [0,2,4,6,8]:
        B //= 2
        answer += 1
    else:
        print(-1)
        break
else:
    print(answer if A == B else -1)