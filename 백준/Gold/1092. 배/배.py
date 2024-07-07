n = int(input())
weight_limit = list(map(int, input().split()))
weight_limit.sort()
m = int(input())
box_weight = list(map(int, input().split()))
box_weight.sort()

if weight_limit[-1] < box_weight[-1]:
    print(-1)
else:
    time = -(- m // n)
    saved = 0
    while True:
        curr_machine = weight_limit.pop()
        saved += 1
        if len(box_weight) <= time:
            break
        for _ in range(time):
            box_weight.pop()
        tmp = 0
        while box_weight and weight_limit[-1] < box_weight[-1]:
            box_weight.pop()
            tmp += 1
        if tmp % saved:
            for _ in range(saved - tmp % saved):
                if box_weight:
                    box_weight.pop()
        time += -(-tmp // saved)
    print(time)