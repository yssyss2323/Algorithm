n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
current_sum = 0
prefix_counts = {0: 1}

for num in arr:
    current_sum += num
    ans += prefix_counts.get(current_sum - k, 0)
    prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
print(ans)