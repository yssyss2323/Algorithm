def calc(arr):
    a, b = arr[0]
    c, d = arr[1]
    return a * a * b * d + a * b * b * c

nums = [list(map(int, input().split())) for _ in range(2)]

val = calc(nums)
ans = 0
for i in range(1, 4):
    nums = [[nums[1][0], nums[0][0]], [nums[1][1], nums[0][1]]]
    curr = calc(nums)
    if curr > val:
        val = curr
        ans = i
print(ans)