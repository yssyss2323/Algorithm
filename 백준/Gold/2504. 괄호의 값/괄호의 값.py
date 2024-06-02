string = input()
stack = []
table = [['(', ')', 2], ['[', ']', 3]]

for ch in string:
    if ch in '([':
        stack.append(ch)
    else:
        val = 0
        for i in range(2):
            if ch == table[i][1]:
                if not stack:
                    print(0)
                    exit()
                while stack:
                    tmp = stack.pop()
                    if tmp == table[i][0]:
                        stack.append(table[i][2] if val == 0 else val*table[i][2])
                        break
                    elif type(tmp) == int:
                        val += tmp
                    else:
                        print(0)
                        exit()
                else:
                    print(0)
                    exit()

answer = 0
for i in stack:
    if type(i) == int:
        answer += i
    else:
        print(0)
        break
else:
    print(answer)
    