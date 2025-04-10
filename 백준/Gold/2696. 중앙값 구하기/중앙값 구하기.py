import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    m = int(input())
    mmlist = []
    for _ in range(m // 10 + 1):
        mmlist += list(map(int, input().split()))

    anslist = [mmlist[0]]

    top_heap = [max(mmlist[:2])]
    bot_heap = [-min(mmlist[:2])]
    top_len = 1
    bot_len = 1

    for i in range(2, m):
        top = heapq.heappop(top_heap)
        bot = -heapq.heappop(bot_heap)
        tmp = mmlist[i]

        tmplist = [bot, tmp, top]
        tmplist.sort()

        if top_len <= bot_len:
            heapq.heappush(top_heap, tmplist[2])
            heapq.heappush(top_heap, tmplist[1])
            heapq.heappush(bot_heap, -tmplist[0])
            top_len += 1
        else:
            heapq.heappush(top_heap, tmplist[2])
            heapq.heappush(bot_heap, -tmplist[1])
            heapq.heappush(bot_heap, -tmplist[0])
            bot_len += 1

        if i % 2 == 0:
            tmp = heapq.heappop(top_heap)
            anslist.append(tmp)
            heapq.heappush(top_heap, tmp)

    length = len(anslist)
    print(length)
    for i in range(length // 10):
        print(*anslist[i * 10:i * 10 + 10])
    print(*anslist[(length // 10) * 10:])