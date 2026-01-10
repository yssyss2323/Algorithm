for _ in range(int(input())):
    cards = list(input().split())
    if len(set(cards)) <= 2:
        print(":)")
    else:
        plist, slist, mlist = [], [], []
        for i in range(4):
            if cards[i][1] == 'p':
                plist.append(int(cards[i][0]))
            elif cards[i][1] == 's':
                slist.append(int(cards[i][0]))
            else:
                mlist.append(int(cards[i][0]))
        plist.sort()
        slist.sort()
        mlist.sort()
        if len(plist) >= 3 and plist[0] + 1 == plist[1] == plist[2] - 1:
            print(":)")
        elif len(plist) == 4 and (plist[1] + 1 == plist[2] == plist[3] - 1 or plist[0] + 1 == plist[1] == plist[3] - 1):
            print(":)")
        elif len(slist) >= 3 and slist[0] + 1 == slist[1] == slist[2] - 1:
            print(":)")
        elif len(slist) == 4 and (slist[1] + 1 == slist[2] == slist[3] - 1 or slist[0] + 1 == slist[1] == slist[3] - 1):
            print(":)")
        elif len(mlist) >= 3 and mlist[0] + 1 == mlist[1] == mlist[2] - 1:
            print(":)")
        elif len(mlist) == 4 and (mlist[1] + 1 == mlist[2] == mlist[3] - 1 or mlist[0] + 1 == mlist[1] == mlist[3] - 1):
            print(":)")
        else:
            print(":(")