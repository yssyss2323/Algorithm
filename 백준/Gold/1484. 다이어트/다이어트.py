g = int(input())
answerlist = []
end = int(g**0.5) if int(g**0.5) == g**0.5 else int(g**0.5) + 1
for i in range(1,end):
    if g % i == 0 and i % 2 == (g // i) % 2:
        answerlist.append((i + g // i) // 2)
if answerlist:
    for i in reversed(answerlist):
        print(i)
else:
    print(-1)