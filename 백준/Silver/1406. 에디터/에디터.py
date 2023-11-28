left = list(input())
right_reverse = []

M = int(input())
for _ in range(M):
    tmp = input()
    if tmp == 'L' and left:
        right_reverse.append(left.pop())
    elif tmp == 'D' and right_reverse:
        left.append(right_reverse.pop())
    elif tmp == 'B' and left:
        left.pop()
    elif tmp[0] == 'P':
        left.append(tmp[2])
right = list(reversed(right_reverse))
print(''.join(left + right))