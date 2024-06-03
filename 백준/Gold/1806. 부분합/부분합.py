N, S = map(int, input().split())
numlist = list(map(int, input().split()))
sumlist = [0] * (N + 1)
sum = 0
for i in range(N):
    sum += numlist[i]
    sumlist[i + 1] = sum

if sumlist[N] < S:
    print(0)
else:
    left, right = 0, 0
    answer = float('inf')
    while True:
        while sumlist[right] - sumlist[left] < S and right < N:
            right += 1
        while sumlist[right] - sumlist[left] >= S:
            left += 1
        answer = min(answer, right - left + 1)
        if right == N:
            break
    print(answer)
