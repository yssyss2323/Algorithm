import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
numlist = []
stack = []
stackcount = {}
for _ in range(n):
    numlist.append(int(input()))
for i in numlist:
    stackcount[i]=0
answer = 0
for num in reversed(numlist):
    while stack and stack[-1] < num:
        tmp = stack.pop()
        stackcount[tmp] -= 1
        answer += 1
    else:
        if stack:
            if stack[-1] == num:
                answer += stackcount[num]
                if len(stack) > stackcount[num]:
                    answer += 1
            else:
                answer += 1
        stack.append(num)
        stackcount[num] += 1
        #print(num,answer,stack,stackcount)
print(answer)