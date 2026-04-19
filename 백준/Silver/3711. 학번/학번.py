def find_smallest_modulus(nums):
    nums.sort()
    n = len(nums)
    max_val = 10 ** 6

    diff_exists = [False] * (max_val + 1)
    for i in range(n):
        for j in range(i + 1, n):
            diff = nums[j] - nums[i]
            diff_exists[diff] = True

    for x in range(n, max_val + 2):
        is_valid = True
        for multiple in range(x, max_val + 1, x):
            if diff_exists[multiple]:
                is_valid = False
                break

        if is_valid:
            return x

for _ in range(int(input())):
    nums = int(input())
    arr = [int(input()) for _ in range(nums)]
    ans = find_smallest_modulus(arr)
    print(ans)