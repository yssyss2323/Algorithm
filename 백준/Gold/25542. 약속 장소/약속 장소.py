n, l = map(int, input().split())

check = set()
cand = input()
for i in range(l):
    for j in range(26):
        tmp_cand = cand[:i] + chr(ord('A') + j) + cand[i+1:]
        check.add(tmp_cand)

for _ in range(n - 1):
    tmp_check = set()
    cand = input()
    for i in range(l):
        for j in range(26):
            tmp_cand = cand[:i] + chr(ord('A') + j) + cand[i+1:]
            tmp_check.add(tmp_cand)
    check = check.intersection(tmp_check)
if check:
    print(check.pop())
else:
    print("CALL FRIEND")