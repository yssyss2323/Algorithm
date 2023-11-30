import sys
T = sys.stdin.readline()
stack, answer = 0, 0
for ii in range(len(T)):
    if T[ii] == '(':
        if T[ii + 1] == '(':
            stack += 1
            answer += 1
        else:  # 레이저
            answer += stack
    else:
        if T[ii - 1] != '(':  # not 레이저
            stack -= 1
print(answer)