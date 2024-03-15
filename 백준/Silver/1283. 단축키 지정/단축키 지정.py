n = int(input())
options = []
for _ in range(n):
    options.append(list(input().split()))
shortcut = []
for option in options:
    for i in range(len(option)):
        key = ord(option[i][0]) % 32
        if key not in shortcut:
            shortcut.append(key)
            option[i] = '[' + option[i][0] + ']' + option[i][1:]
            break
    else:
        for i in range(len(option)):
            for j in range(1, len(option[i])):
                key = ord(option[i][j]) % 32
                if key not in shortcut:
                    shortcut.append(key)
                    option[i] = option[i][:j] + '[' + option[i][j] + ']' + option[i][j + 1:]
                    break
            if '[' in option[i]:
                break
for answer in options:
    print(*answer)
