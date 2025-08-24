import sys
input = lambda:sys.stdin.readline().rstrip()

check = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

while True:
    word = input()
    if word == '#':
        break
    ans = []
    for i in range(len(word) - 1, -1, -1):
        ch = word[i]
        if ch in check.keys():
            ans.append(check[ch])
        elif ch in 'iovwx':
            ans.append(ch)
        else:
            ans = list("INVALID")
            break
    print("".join(ans))