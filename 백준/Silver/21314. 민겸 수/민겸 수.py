mk_num = input()

stack = []
large, small = '', ''
for ch in mk_num:
    if ch == 'M':
        stack.append('M')
    else:
        large += '5' + len(stack) * '0'
        if stack:
            small += '1' + (len(stack) - 1) * '0' + '5'
        else:
            small += '5'
        stack.clear()
if stack:
    large += len(stack) * '1'
    small += '1' + (len(stack) - 1) * '0'

print(large)
print(small)