expression = input()

stack = []
idx_list = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        stack.append(i)
    if ch == ')':
        idx = (stack.pop(), i)
        idx_list.append(idx)
idx_list.sort()

n = len(idx_list)
dup_check = set()
for i in range(1, 2 ** n):
    explist = list(expression)
    tmp = bin(i)[2:]
    tmp = (n - len(tmp)) * '0' + tmp
    #print(n,tmp)
    for j in range(n):
        if tmp[j] == '1':
            l, r = idx_list[j]
            explist[l] = ''
            explist[r] = ''
    ans = ''.join(explist)
    if ans not in dup_check:
        dup_check.add(ans)

anslist = list(dup_check)
anslist.sort()
for ans in anslist:
    print(ans)