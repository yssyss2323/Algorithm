r, c = map(int, input().split())
puzzle = [list(input()) for _ in range(r)]
words = []

for i in range(c):
    word = ''
    for j in range(r):
        if puzzle[j][i] != '#':
            word += puzzle[j][i]
        else:
            if len(word) >= 2:
                words.append(word)
            word = ''
    if len(word) >= 2:
        words.append(word)

for i in range(r):
    word = ''
    for j in range(c):
        if puzzle[i][j] != '#':
            word += puzzle[i][j]
        else:
            if len(word) >= 2:
                words.append(word)
            word = ''
    if len(word) >= 2:
        words.append(word)

words.sort()
print(words[0])