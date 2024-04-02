T = int(input())
for _ in range(T):
    testcase = input()
    score = 0
    for i in testcase:
        score += 1 if i == '(' else -1
        if score < 0:
            print("NO")
            break
    else:
        print("NO" if score else "YES")
