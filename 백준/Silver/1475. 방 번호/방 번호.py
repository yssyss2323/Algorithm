num = input()
checklist = []
special = 0
for i in range(10):
    if i == 6 or i == 9:
        special += num.count(str(i))
    else:
        checklist.append(num.count(str(i)))
else:
    checklist.append((special+1)//2)
print(max(checklist))