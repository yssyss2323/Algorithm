n, k = map(int, input().split())
size = list(map(int, input().split()))
gap = [size[i + 1] - size[i] for i in range(n - 1)]
gap.sort(reverse=True)
ans = sum(gap[k - 1:])
print(ans)