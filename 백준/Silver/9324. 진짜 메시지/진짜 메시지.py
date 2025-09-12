for _ in range(int(input())):
    message = input()
    check ={chr(i) : 0 for i in range(ord('A'), ord('Z') + 1)}
    length = len(message)
    for i in range(length):
        ch = message[i]
        check[ch] += 1
        if check[ch] == 3:
            if i + 1 >= length or message[i + 1] != ch:
                print("FAKE")
                break
            check[ch] = -1
    else:
        print("OK")
