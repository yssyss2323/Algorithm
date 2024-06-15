import sys

input = lambda:sys.stdin.readline().rstrip()
N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    address, secret = input().split()
    memo[address] = secret
for _ in range(M):
    print(memo[input()])
