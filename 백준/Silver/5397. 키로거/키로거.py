T = int(input())
for _ in range(T):
    key_log = input()
    cursor = 0
    left, right_reverse = [], []
    for key in key_log:
        if key == '-':
            if left:
                left.pop()
        elif key == '<':
            if left:
                right_reverse.append(left.pop())
        elif key == '>':
            if right_reverse:
                left.append(right_reverse.pop())
        else:
            left.append(key)
    right = right_reverse[::-1]
    answer_left = ''.join(left)
    answer_right = ''.join(right)
    print(answer_left + answer_right)
