N, M = map(int, input().split())
not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input())

for _ in range(M):
    not_seen.add(input())

result = sorted(list(not_heard & not_seen))
print(len(result))
for name in result:
    print(name)