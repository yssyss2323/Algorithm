n = int(input())
k = int(input())
coord = list(set(map(int, input().split())))
coord.sort()

gap = [coord[i + 1] - coord[i] for i in range(len(coord) - 1)]
gap.sort(reverse=True)

print(sum(gap[k - 1:]))