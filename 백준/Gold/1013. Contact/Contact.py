from collections import deque

n = int(input())
for _ in range(n):
    curr = deque(input())
    while curr:
        ch = curr.popleft()
        if ch == '1':
            cnt = 0
            while curr and curr[0] == '0':
                curr.popleft()
                cnt += 1
            if cnt < 2 or not curr:
                print('NO')
                break
            else:
                cnt = 0
                while curr and curr[0] == '1':
                    curr.popleft()
                    cnt += 1
                if cnt >= 2 and len(curr) >= 2 and curr[0] == '0' and curr[1] == '0':
                    curr.appendleft('1')
        else:
            if not curr or curr.popleft() == '0':
                print('NO')
                break
            else:
                while len(curr) >= 2 and curr[0] == '0' and curr[1] == '1':
                    curr.popleft()
                    curr.popleft()
    else:
        print('YES')