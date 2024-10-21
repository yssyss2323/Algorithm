s = input()

while s:
    if s[0] == 'p':
        if len(s) >= 2 and s[:2] == "pi":
            s = s[2:]
        else:
            print("NO")
            break
    elif s[0] == 'k':
        if len(s) >= 2 and s[:2] == "ka":
            s = s[2:]
        else:
            print("NO")
            break
    elif s[0] == 'c':
        if len(s) >= 3 and s[:3] == "chu":
            s = s[3:]
        else:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")