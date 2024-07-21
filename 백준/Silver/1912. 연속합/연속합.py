num_integer = int(input())
num_list = [0] + list(map(int, input().split()))
sum_list = []
tmp = 0
for num in num_list:
    tmp += num
    sum_list.append(tmp)

min_num = sum_list[0]
ans = -float('inf')
for i in range(1, num_integer + 1):
    if sum_list[i] - min_num > ans:
        ans = sum_list[i] - min_num
    if sum_list[i] < min_num:
        min_num = sum_list[i]
print(ans)