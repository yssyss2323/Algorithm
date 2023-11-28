word = input()
english = 'abcdefghijklmnopqrstuvwxyz'
answerlist = []
for i in english:
    answerlist.append(str(word.count(i)))
answer = ' '.join(answerlist)
print(answer)