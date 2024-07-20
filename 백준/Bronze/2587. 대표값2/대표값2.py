numlist = [int(input()) for _ in range(5)]
numlist.sort()
print(sum(numlist) // 5)
print(numlist[2])