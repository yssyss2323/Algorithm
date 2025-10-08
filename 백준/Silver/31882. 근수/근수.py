def score_k(cnt):
    return cnt * (cnt + 1) * (cnt + 2) // 6

n = int(input())
s = input()
idx = 0
ans = 0
while idx < n:
    if s[idx] != '2':
        idx += 1
        continue
    else:
        cnt = 0
        while idx < n and s[idx] == '2':
            idx += 1
            cnt += 1
        ans += score_k(cnt)
print(ans)