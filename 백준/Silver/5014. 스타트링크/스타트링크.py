from collections import deque

# 초기화
f, s, g, u, d = map(int, input().split())
building = ['None'] + [False] * f # 층수와 index를 맞추기 위해 None 추가
q = deque([[s,0]]) # 처음 위치 s를 큐에 추가
building[s] = True # s층은 방문한 것으로 갱신

# bfs 수행 : 현재 층에서 1) u만큼 올라가거나 2) d만큼 내려간 경우를 탐색
while q:
    now, num = q.popleft()

    # 목표층 g에 도달한 경우
    if now == g:
        print(num)
        break

    nextup, nextdown, num = now + u, now - d, num + 1

    # u층 위로 이동
    if nextup <= f and not building[nextup]:
        q.append([nextup, num])
        building[nextup] = True

    # d층 아래로 이동
    if nextdown >= 1 and not building[nextdown]:
        q.append([nextdown, num])
        building[nextdown] = True
else:
    print("use the stairs")