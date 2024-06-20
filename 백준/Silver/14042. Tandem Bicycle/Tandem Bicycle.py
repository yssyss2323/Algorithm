q = int(input())
n = int(input())
country1 = list(map(int, input().split()))
country2 = list(map(int, input().split()))
if q == 1:
    country1.sort()
    country2.sort()
else:
    country1.sort(reverse=True)
    country2.sort()

ans = 0
for i in range(n):
    ans += max(country1[i], country2[i])
print(ans)