import sys
input = sys.stdin.readline


def transform(x):
    if x == '0':
        return '0'
    if x == '-':
        return '1'
    if x == '+':
        return '2'


n = int(input())

relation = [''.join(map(transform, input().split())) for _ in range(n)]

for _ in range(int(input())):
    b, c = map(int, input().split())
    if relation[b][c] == '2':
        print('+')
    else:
        print('-')
