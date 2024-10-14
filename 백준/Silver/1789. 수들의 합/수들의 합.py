s = int(input())
tmp = int((s * 2) ** 0.5)
if tmp * (tmp - 1) // 2 <= s < tmp * (tmp + 1) // 2:
    print(tmp - 1)
elif tmp * (tmp + 1) // 2 <= s < (tmp + 2) * (tmp + 1) // 2:
    print(tmp)