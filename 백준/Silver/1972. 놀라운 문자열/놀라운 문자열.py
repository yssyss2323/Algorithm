while True:
    string = input()
    if string == "*":
        break

    flag = False
    for i in range(1, len(string)):
        check = set()
        for j in range(len(string) - i):
            tmp = string[j] + string[i + j]
            if tmp in check:
                print(f"{string} is NOT surprising.")
                flag = True
                break
            else:
                check.add(tmp)
        if flag:
            break
    else:
        print(f"{string} is surprising.")