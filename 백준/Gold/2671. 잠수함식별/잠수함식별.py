from collections import deque

sound = deque(input())

while sound:
    # print(sound)
    ch = sound.popleft()
    if ch == '1':
        if len(sound) >= 3 and sound[0] == '0' and sound[1] == '0':
            while sound and sound[0] == '0':
                sound.popleft()
            if not sound:
                print("NOISE")
                break
            check = 0
            while sound and sound[0] == '1':
                sound.popleft()
                check += 1
            if check >= 2 and len(sound) >= 2 and sound[0] == '0' and sound[1] == '0':
                sound.appendleft('1')
        else:
            print("NOISE")
            break
    else:
        if len(sound) >= 1 and sound[0] == '1':
            sound.popleft()
        else:
            print("NOISE")
            break
else:
    print("SUBMARINE")