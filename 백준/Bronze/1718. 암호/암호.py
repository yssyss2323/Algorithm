string = input()
key = input()

for i in range(len(string)):
    k = ord(' ')
    if string[i] != ' ':
        k = ord(string[i]) - (ord(key[i % len(key)]) - ord('a') + 1)
        if k < ord('a'):
            k += ord('z') - ord('a') + 1
    print(chr(k), end='')