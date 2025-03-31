def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    ans = 1
    for i in range(len(nums) - 1):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            tmp = gcd(num1, num2)
            if tmp > ans:
                ans = tmp

    print(ans)