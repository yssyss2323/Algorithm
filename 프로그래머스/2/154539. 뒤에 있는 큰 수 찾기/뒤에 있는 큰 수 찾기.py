def solution(numbers):
    answer = []
    stack = []
    for i in reversed(numbers):
        while stack:
            if stack[-1] <= i:
                stack.pop()
            else:
                answer.append(stack[-1])
                stack.append(i)
                break
        else:
            stack.append(i)
            answer.append(-1)
    answer.reverse()
    return answer