while True:
    try:
        s,t = input().split()
        idx = 0
        for ch in t:
            if ch == s[idx]:
                idx += 1
            if idx == len(s):
                print("Yes")
                break
        else:
            print("No")
    except:
        break
