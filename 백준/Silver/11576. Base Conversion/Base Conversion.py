a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

origin = 0
for i in reversed(range(m)):
    origin += nums[i] * a ** (m - i - 1)

ans = []
while origin >= b:
    ans.append(origin % b)
    origin //= b
if origin > 0:
    ans.append(origin)

print(*ans[::-1])
