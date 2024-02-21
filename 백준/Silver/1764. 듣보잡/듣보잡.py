n,m = map(int,input().split())
not_heard, not_seen = [], set()
for _ in range(n):
    not_heard.append(input())
not_heard.sort()
for _ in range(m):
    not_seen.add(input())

answer = []
for i in not_heard:
    if i in not_seen:
        answer.append(i)

print(len(answer))
for i in answer:
    print(i)