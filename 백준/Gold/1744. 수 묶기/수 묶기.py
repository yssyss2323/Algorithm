n = int(input())
pos_num = []
neg_num = []
one = 0
zero = 0
for _ in range(n):
    tmp = int(input())
    if tmp > 0:
        if tmp == 1:
            one += 1
        else:
            pos_num.append(tmp)
    elif tmp < 0:
        neg_num.append(-tmp)
    else:
        zero += 1
pos_num.sort()
neg_num.sort()

ans = one
for i in range(len(pos_num) // 2):
    num1 = pos_num.pop()
    num2 = pos_num.pop()
    ans += num1 * num2
    # ans += pos_num[i * 2 + 1] * pos_num[i * 2]
if pos_num:
    ans += pos_num[0]

for i in range(len(neg_num) // 2):
    num1 = neg_num.pop()
    num2 = neg_num.pop()
    ans += num1 * num2
    # ans += neg_num[i * 2 + 1] * neg_num[i * 2]
if neg_num:
    if zero == 0:
        ans -= neg_num[0]

print(ans)