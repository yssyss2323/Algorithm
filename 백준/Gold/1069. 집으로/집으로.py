X, Y, D, T = map(int, input().split())
distance = (X ** 2 + Y ** 2) ** 0.5

if D < T:
    print(distance)
else:
    tmp = distance // D
    case1 = T * tmp + distance - D * tmp
    case2 = T * (tmp + 1) if tmp else T * 2
    case3 = T * (tmp + 1) + D * (tmp + 1) - distance
    print(min(case1, case2, case3))
