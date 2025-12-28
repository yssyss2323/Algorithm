import sys
input = lambda : sys.stdin.readline().rstrip()

def check(string):
    length = len(string)
    if length == 1:
        return True
    check_len = len(string) // 2
    for i in range(check_len):
        if string[i] == string[length - i - 1]:
            return False
    else:
        return check(string[:check_len])

for _ in range(int(input())):
    if check(input()):
        print("YES")
    else:
        print("NO")
