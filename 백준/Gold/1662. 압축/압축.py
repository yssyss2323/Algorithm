def decompress(string):
    string += 'x'
    ans = 0
    i = 0
    while i < len(string) - 1:
        if string[i + 1] != '(':
            ans += 1
            i += 1
        else:
            stack = ['(']
            substring = []
            length_num = 0
            j = i + 1
            while stack:
                j += 1
                substring.append(string[j])
                if string[j] in '1234567890':
                    length_num += 1
                else:
                    if string[j] == '(':
                        stack.append('(')
                    else:
                        stack.pop()
            ans += int(string[i]) * decompress(substring[:-1])
            i = j + 1
    return ans


s = input()
print(decompress(s))
