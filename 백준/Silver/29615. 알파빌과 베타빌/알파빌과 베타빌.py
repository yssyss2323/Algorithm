n, m = map(int, input().split())

waitlist = list(map(int, input().split()))
friends = list(map(int, input().split()))

cnt = 0
for friend in friends:
    if friend in waitlist[:m]:
        cnt += 1

print(m - cnt)