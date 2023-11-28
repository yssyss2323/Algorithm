import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
answer = 0
for _ in range(N):
    ABstring = input()
    stack = []
    for chr in ABstring:
        if stack and chr == stack[-1]:
            stack.pop()
        else:
            stack.append(chr)
    if not stack:
        answer += 1
print(answer)