from collections import deque

s = input()
t = input()
length = len(t)

q = deque([s])
while q:
    curr_s = q.popleft()
    #print(curr_s, rev)
    if len(curr_s) > length:
        print(0)
        break
    if len(curr_s) == length:
        check = ''.join(curr_s)
        if check == t:
            print(1)
            break
    next_s1 = curr_s + 'A'
    if next_s1 in t or next_s1[::-1] in t:
        q.append(next_s1)
    next_s2 = 'B' + curr_s[::-1]
    if next_s2 in t or next_s2[::-1] in t:
        q.append(next_s2)
else:
    print(0)