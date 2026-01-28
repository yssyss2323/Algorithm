def check(num):
    for i in range(1, len(num)):
        front = 1
        for j in range(i):
            front *= int(num[j])
        back = 1
        for j in range(i, len(num)):
            back *= int(num[j])
        if front == back:
            print("YES")
            break
    else:
        print("NO")

check(input())