def transform(word):
    word = word.replace('k','c')
    word = word.replace('ng', 'nz')
    return word

def re_transform(word):
    word = word.replace('nz','ng')
    word = word.replace('c','k')
    return word

n = int(input())
words = [transform(input()) for _ in range(n)]
words.sort()
for word in words:
    print(re_transform(word))