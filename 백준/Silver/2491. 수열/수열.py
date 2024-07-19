length_of_nums = int(input())
numlist = list(map(int, input().split()))

record = [0, 0]
curr_length = [1, 1]
curr_num = numlist[0]
for i in range(1, length_of_nums):
    next_num = numlist[i]
    if next_num > curr_num:
        curr_length[0] += 1
        record[1] = max(record[1], curr_length[1])
        curr_length[1] = 1
    elif next_num < curr_num:
        curr_length[1] += 1
        record[0] = max(record[0], curr_length[0])
        curr_length[0] = 1
    else:
        curr_length[0] += 1
        curr_length[1] += 1
    curr_num = next_num
print(max(record + curr_length))
