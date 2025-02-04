def case(arr):
    case_list = [
        [arr[0], arr[1], arr[2], arr[3]],
        [arr[0], arr[3], arr[1], arr[2]],
        [arr[0], arr[2], arr[3], arr[1]],
        [arr[1], arr[0], arr[3], arr[2]],
        [arr[1], arr[2], arr[0], arr[3]],
        [arr[1], arr[3], arr[2], arr[0]],
        [arr[2], arr[3], arr[0], arr[1]],
        [arr[2], arr[1], arr[3], arr[0]],
        [arr[2], arr[0], arr[1], arr[3]],
        [arr[3], arr[0], arr[2], arr[1]],
        [arr[3], arr[1], arr[0], arr[2]],
        [arr[3], arr[2], arr[1], arr[0]]
    ]
    return case_list

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d, e, f, g, h = map(int, input().split())
    for arr in case([a, b, c, d]):
        if [e, f, g, h] == arr:
            print(1)
            break
    else:
        print(0)