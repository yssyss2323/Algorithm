word1 = input()
word2 = input()
answer = 0
wordlist = set(word1+word2)
for word in wordlist:
    answer += abs(word1.count(word) - word2.count(word))
print(answer)