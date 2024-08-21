t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    s, m = 0, 100
    for num in nums:
        if num % 2 == 0:
            s += num
            if num < m:
                m = num
    print(s, m)
