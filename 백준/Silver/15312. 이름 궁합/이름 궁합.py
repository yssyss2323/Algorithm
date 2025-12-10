a = input()
b = input()

check = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

nums = []
for i in range(len(a)):
    nums.append(check[ord(a[i]) - ord('A')])
    nums.append(check[ord(b[i]) - ord('A')])

while len(nums) > 2:
    tmp = []
    for i in range(len(nums) - 1):
        tmp.append((nums[i] + nums[i + 1]) % 10)
    nums = tmp
ans = str(nums[0]) + str(nums[1])
print(ans)