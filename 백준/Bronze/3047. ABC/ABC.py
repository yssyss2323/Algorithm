arr = list(map(int, input().split()))
arr.sort()
check = {'A':arr[0], 'B':arr[1], 'C':arr[2]}

ans = [check[ch] for ch in input()]
print(*ans)