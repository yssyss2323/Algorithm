while True:
    curr = input()
    if curr == '#':
        break

    ch, string = curr[0], curr[2:].lower()
    print(ch, string.count(ch))