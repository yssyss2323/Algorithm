N = int(input())
card_nums = list(map(int, input().split()))
card_nums.sort()

M = int(input())
given_nums = list(map(int, input().split()))

answer = []
for num in given_nums:
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        check = card_nums[mid]
        if num == check:
            answer.append(1)
            break
        elif num < check:
            end = mid - 1
        else:
            start = mid + 1
    else:
        answer.append(0)
print(*answer)
