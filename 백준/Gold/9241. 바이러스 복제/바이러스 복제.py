def solve():
    origin = input()
    later = input()

    startidx = 0
    min_len = min(len(origin), len(later))

    while startidx < min_len and origin[startidx] == later[startidx]:
        startidx += 1

    origin_endidx = len(origin) - 1
    later_endidx = len(later) - 1

    while (
        origin_endidx >= startidx
        and later_endidx >= startidx
        and origin[origin_endidx] == later[later_endidx]
    ):
        origin_endidx -= 1
        later_endidx -= 1

    if startidx >= min_len - (len(origin) - 1 - origin_endidx):
        if len(origin) > len(later):
            print(0)
        else:
            print(len(later) - len(origin))
    else:
        print(len(later) - startidx - (len(origin) - 1 - origin_endidx))


if __name__ == "__main__":
    solve()