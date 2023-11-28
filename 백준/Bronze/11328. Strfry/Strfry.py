N = int(input())
wordlist = []
for i in range(N):
    wordlist.append(input().split())
for words in wordlist:
    if sorted(words[0]) == sorted(words[1]):
        print("Possible")
    else:
        print("Impossible")