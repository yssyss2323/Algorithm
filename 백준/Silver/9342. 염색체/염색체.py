t = int(input())
for _ in range(t):
    string = input()

    check = True

    if string[0] not in 'ABCDEF':
        check = False
    else:
        if string[0] != 'A':
            string = string[1:]
        if not string or string[0] != 'A':
            check = False
        else:
            while string and string[0] == 'A':
                string = string[1:]

            if not string or string[0] != 'F':
                check = False
            else:
                while string and string[0] == 'F':
                    string = string[1:]

                if not string or string[0] != 'C':
                    check = False
                else:
                    while string and string[0] == 'C':
                        string = string[1:]

                    if not (len(string) == 0 or (len(string) == 1 and string in 'ABCDEF')):
                        check = False
    if check:
        print("Infected!")
    else:
        print("Good")