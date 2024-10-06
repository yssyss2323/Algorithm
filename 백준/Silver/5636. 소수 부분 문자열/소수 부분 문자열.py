prime = [False] * 2 + [True] * 99999
check = []
for i in range(2, 100001):
    if prime[i]:
        check.append(i)
        for j in range(i * 2, 100001, i):
            prime[j] = False
check.reverse()

while True:
    string = input()
    if string == '0':
        break

    for i in check:
        if str(i) in string:
            print(i)
            break