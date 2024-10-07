n = int(input())
numlist = list(map(int, input().split()))
operations = list(map(int, input().split()))

def bt(check, val):
    cnt = sum(check)
    if cnt == n - 1:
        anslist.append(val)
    else:
        if check[0] < operations[0]:
            next_val = val + numlist[cnt + 1]
            check[0] += 1
            bt(check, next_val)
            check[0] -= 1
        if check[1] < operations[1]:
            next_val = val - numlist[cnt + 1]
            check[1] += 1
            bt(check, next_val)
            check[1] -= 1
        if check[2] < operations[2]:
            next_val = val * numlist[cnt + 1]
            check[2] += 1
            bt(check, next_val)
            check[2] -= 1
        if check[3] < operations[3]:
            sign = val // abs(val) if val else 1
            next_val = sign * (abs(val) // numlist[cnt + 1])
            check[3] += 1
            bt(check, next_val)
            check[3] -= 1

anslist = []
bt([0, 0, 0, 0], numlist[0])
anslist.sort()
print(anslist[-1])
print(anslist[0])
