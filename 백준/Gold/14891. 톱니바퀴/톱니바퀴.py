from collections import deque

gears = []
for _ in range(4):
    gears.append(deque(map(int, input())))

k = int(input())
for _ in range(k):
    gear_num, clock = map(int, input().split())

    if gear_num == 1:
        if gears[0][2] != gears[1][6]:
            if gears[1][2] != gears[2][6]:
                if gears[2][2] != gears[3][6]:
                    gears[3].rotate(-clock)
                gears[2].rotate(clock)
            gears[1].rotate(-clock)
        gears[0].rotate(clock)

    elif gear_num == 2:
        if gears[1][6] != gears[0][2]:
            gears[0].rotate(-clock)
        if gears[1][2] != gears[2][6]:
            if gears[2][2] != gears[3][6]:
                gears[3].rotate(clock)
            gears[2].rotate(-clock)
        gears[1].rotate(clock)

    elif gear_num == 3:
        if gears[2][6] != gears[1][2]:
            if gears[1][6] != gears[0][2]:
                gears[0].rotate(clock)
            gears[1].rotate(-clock)
        if gears[2][2] != gears[3][6]:
            gears[3].rotate(-clock)
        gears[2].rotate(clock)

    else:
        if gears[3][6] != gears[2][2]:
            if gears[2][6] != gears[1][2]:
                if gears[1][6] != gears[0][2]:
                    gears[0].rotate(-clock)
                gears[1].rotate(clock)
            gears[2].rotate(-clock)
        gears[3].rotate(clock)

print(sum(gears[i][0] * 2 ** i for i in range(4)))