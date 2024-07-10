import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
word_dic = dict()
for _ in range(n):
    word = input()
    if len(word) < m:
        continue
    word_dic[word] = word_dic.get(word, [word, len(word), 0])
    word_dic[word][2] += 1
anslist = list(word_dic.values())
anslist.sort(key= lambda x: (-x[2], -x[1], x[0]))
for ans in anslist:
    print(ans[0])