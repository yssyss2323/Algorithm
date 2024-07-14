from collections import Counter

n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp_cnt = Counter(tmp[1:])
    if tmp_cnt.most_common(1)[0][1] > tmp[0] // 2:
        print(tmp_cnt.most_common(1)[0][0])
    else:
        print("SYJKGW")