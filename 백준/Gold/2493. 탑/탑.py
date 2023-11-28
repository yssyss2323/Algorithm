import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
toplist = list(map(int,input().split()))

stack = []
answerlist = []
for i in range(n):
    while stack:
        if toplist[stack[-1]] < toplist[i]:
            stack.pop()
        else:
            answerlist.append(stack[-1]+1)
            break
    else:
        answerlist.append(0)
    stack.append(i)
print(*answerlist)