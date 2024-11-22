n = int(input())
levels = [int(input()) for _ in range(n)]

ans = 0
for i in range(n - 2, -1, -1):
    curr_lv = levels[i + 1]
    prev_lv = levels[i]
    if prev_lv >= curr_lv:
        ans += prev_lv - (curr_lv - 1)
        levels[i] = curr_lv - 1
print(ans)
