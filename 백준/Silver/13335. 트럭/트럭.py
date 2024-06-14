from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
q = deque([0] * w)
total_weight = 0

time = 0
for i in range(n):
    truck = trucks[i] # 다리에 올라가려는 트럭
    while True:
        # step 1 : 다리의 끝에 도달한 트럭 내보내기
        total_weight -= q[0]
        q[0] = 0
        # step 2 : 다리상태 업데이트 및 시간 갱신
        q.rotate(-1)
        time += 1
        # step 3 : 현재 트럭이 올라가도 무게제한에 안걸리면 트럭 진입
        if total_weight + truck <= L:
            q[w - 1] = truck
            total_weight += truck
            break

print(time + w) # 위 로직상 마지막 트럭이 진입하면 반복문 종료 -> w를 더해줘야 함
