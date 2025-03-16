n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

ans = []
while A or B:
    tmp1 = set(A)
    tmp2 = set(B)
    tmp = tmp1.intersection(tmp2)
    if not tmp:
        break
    num = max(tmp)
    A = A[A.index(num) + 1:]
    B = B[B.index(num) + 1:]
    ans.append(num)
print(len(ans))
print(*ans)