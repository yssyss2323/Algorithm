n = int(input())
shortcut = []
for _ in range(n):
    option = input().split()
    for i in range(len(option)):
        if option[i][0].lower() not in shortcut:
            shortcut.append(option[i][0].lower())
            option[i] = '[' + option[i][0] + ']' + option[i][1:]
            break
    else:
        for i in range(len(option)):
            for j in range(len(option[i])):
                if option[i][j].lower() not in shortcut:
                    shortcut.append(option[i][j].lower())
                    option[i] = option[i][:j] + '[' + option[i][j] + ']' + option[i][j + 1:]
                    break
            if '[' in option[i]:
                break
    print(*option)
