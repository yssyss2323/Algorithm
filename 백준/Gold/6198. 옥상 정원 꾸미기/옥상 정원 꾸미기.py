import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
toplist = []
for _ in range(n):
    toplist.append(int(input()))
stack = []
answerlist = []
for i in range(n-1,-1,-1):
    while stack:
        if toplist[stack[-1]] < toplist[i]:
            stack.pop()
        else:
            answerlist.append(stack[-1]-i-1)
            break
    else:
        answerlist.append(n-i-1)
    stack.append(i)
print(sum(answerlist))