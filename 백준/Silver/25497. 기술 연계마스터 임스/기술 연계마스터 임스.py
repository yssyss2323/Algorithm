n = int(input())
skills = list(input())
stack1, stack2 = 0, 0

ans = 0
for skill in skills:
    if skill in "1234567890":
        ans += 1
    else:
        if skill == "L":
            stack1 += 1
        elif skill == "S":
            stack2 += 1
        elif skill == "R":
            if stack1 > 0:
                ans += 1
                stack1 -= 1
            else:
                print(ans)
                break
        else:
            if stack2 > 0:
                ans += 1
                stack2 -= 1
            else:
                print(ans)
                break
else:
    print(ans)
