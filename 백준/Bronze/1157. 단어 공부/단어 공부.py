from collections import Counter
tmp = input().upper()
check = Counter(tmp).most_common(2)
if len(check) == 1:
    print(check[0][0])
else:
    if check[0][1] > check[1][1]:
        print(check[0][0])
    else:
        print('?')
