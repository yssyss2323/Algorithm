table = dict()
for i in range(ord('A'), ord('Z') + 1):
    table[chr(i)] = i - ord('A')
for i in range(0, 10):
    table[str(i)] = i + 26
table[' '] = 36

rev_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V',
             'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
string = input()
if len(string) % n:
    string += ' ' * (n - len(string) % n)

trans_num = []
for ch in string:
    trans_num.append(table[ch])

new_trans_num = []
for i in range(len(trans_num) // n):
    tmp = [0] * n
    for j in range(n):
        for k in range(n):
            tmp[j] += matrix[j][k] * trans_num[i * n + k]
        tmp[j] %= 37
    new_trans_num += tmp

ans = ''
for i in new_trans_num:
    ans += rev_table[i]
print(ans)
