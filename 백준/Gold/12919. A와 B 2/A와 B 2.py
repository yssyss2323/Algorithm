from collections import deque

s = input()
t = input()
rev_t = t[::-1]
length = len(t)

q = deque([(s, False)])
while q:
    curr_s, rev = q.popleft()
    #print(curr_s, rev)
    if len(curr_s) > length:
        print(0)
        break
    if len(curr_s) == length:
        check = ''.join(curr_s)
        if (rev and check == rev_t) or (not rev and check == t):
            print(1)
            break
    if rev:
        next_s1 = 'A' + curr_s
        if next_s1 in t or next_s1 in rev_t:
            q.append((next_s1, True))
        next_s2 = 'B' + curr_s
        if next_s2 in t or next_s2 in rev_t:
            q.append((next_s2, False))
    else:
        next_s1 = curr_s + 'A'
        if next_s1 in t or next_s1 in rev_t:
            q.append((next_s1, False))
        next_s2 = curr_s + 'B'
        if next_s2 in t or next_s2 in rev_t:
            q.append((next_s2, True))
else:
    print(0)