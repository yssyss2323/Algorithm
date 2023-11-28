import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for chr in sentence:
        if chr in '([':
            stack.append(chr)
        elif chr == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif chr ==']':
            if not stack or stack.pop() != '[':
                print('no')
                break
    else:
        print('yes' if not stack else 'no')