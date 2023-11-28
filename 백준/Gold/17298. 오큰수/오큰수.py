import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
numlist = list(map(int,input().split()))
stack = []
answerlist = []
for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] <= numlist[i]:
            stack.pop()
        else:
            answerlist.append(stack[-1])
            stack.append(numlist[i])
            break
    else:
        stack.append(numlist[i])
        answerlist.append(-1)
answerlist.reverse()
print(*answerlist)