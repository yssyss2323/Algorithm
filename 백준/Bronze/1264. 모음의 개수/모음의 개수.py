vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    sentence = input()
    if sentence == '#':
        break
    cnt = 0
    for ch in vowel:
        cnt += sentence.count(ch)
    print(cnt)