n = int(input())
nums = list(map(int, input().split()))
check_nums = set(nums)
max_num = max(nums)

score = [0] * (max_num + 1)
for num in nums:
    for i in range(2 * num, max_num + 1, num):
        if i in check_nums:
            score[num] += 1
            score[i] -= 1
ans = [score[num] for num in nums]
print(*ans)