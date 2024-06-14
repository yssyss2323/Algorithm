N = int(input())
M = int(input())
S = input()

length = 2 * N + 1
idx = 0
cnt_list = []
while idx < M:
    if S[idx] == 'I':
        cnt = 1
        for i in range(idx + 1, M - 1, 2):
            if S[i] == 'O' and S[i + 1] == 'I':
                cnt += 2
            else:
                break
        if cnt > 1:
            cnt_list.append(cnt)
        idx += cnt
    else:
        idx += 1

answer = 0
for cnt in cnt_list:
    if cnt >= length:
        answer += 1 + (cnt - length) // 2
print(answer)
