word = input()

while word:
    if word[0] != "w":
        print(0)
        break
    cnt = 0
    while word and word[0] == "w":
        word = word[1:]
        cnt += 1
    if len(word) < cnt * 3:
        print(0)
        break
    if word[:cnt * 3] != "o" * cnt + "l" * cnt + "f" * cnt:
        print(0)
        break
    word = word[cnt * 3:]
else:
    print(1)