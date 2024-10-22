n = int(input())
ans = sum(map(int, input().split()))
alist = list(map(int, input().split()))
alist.sort()

for i, a in enumerate(alist):
    ans += i * a

print(ans)
