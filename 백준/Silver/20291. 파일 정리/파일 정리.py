import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
ansdic = dict()
for _ in range(n):
    file_name, category = input().split('.')
    ansdic[category] = ansdic.get(category, 0) + 1
for key in sorted(ansdic.keys()):
    print(key, ansdic[key])