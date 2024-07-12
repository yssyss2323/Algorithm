k = int(input())
n = int(input())

# f는 대문자 영어를 숫자로 바꿔주는 함수
def f(ch):
    return ord(ch) - 65
start_order = list(range(k))
final_order = list(map(f, input()))

# prev에는 물음푤아ㅣㄴ 직전, after에는 물음표라인 직후상태를 저장할 예정
prev, after = start_order, final_order

# prev 구하기
idx = 0
for i in range(n):
    ladder_line = input()
    if ladder_line[0] == '?':
        idx = i
        break
    for j in range(k-1):
        if ladder_line[j] == '-':
            prev[j], prev[j+1] = prev[j+1], prev[j]

# after 구하기
after_orderlist = []
for _ in range(idx + 1, n):
    after_orderlist.append(input())
for order in after_orderlist[::-1]:
    for j in range(k-1):
        if order[j] == '-':
            after[j], after[j+1] = after[j+1], after[j]

# prev와 after를 비교하며 물음표라인 추측
ans = []
i = 0
for i in range(k-1):
    if prev[i] == after[i]:
        ans.append('*')
    else:
        if prev[i+1] == after[i] and prev[i] == after[i+1]:
            prev[i], prev[i+1] = prev[i+1], prev[i]
            ans.append('-')
        else:
            print('x' * (k-1))
            break
else:
    print(''.join(ans))