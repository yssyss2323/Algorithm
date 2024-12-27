import sys
input = lambda:sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        break
    words = []
    for _ in range(n):
        tmp = input()
        words.append((tmp.lower(), tmp))
    words.sort()
    print(words[0][1])