nums = list(map(int, input().split()))
nums.sort()
num1, num2, num3 = nums

if num2 - num1 == num3 - num2:
    print(num3 * 2 - num2)
elif num2 - num1 == 2 * (num3 - num2):
    print(num1 + num3 - num2)
else:
    print(num2 * 2 - num1)