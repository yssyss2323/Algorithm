n, m = map(int, input().split())
seg_height = 1
while (2 ** (seg_height - 1) < n):
    seg_height += 1
seg_tree = [0] * (2 ** seg_height)
first_idx = 2 ** (seg_height - 1)
seg_tree[first_idx:first_idx + n] = list(map(int, input().split()))

curr_height = seg_height - 1
while curr_height > 0:
    for i in range(2 ** (curr_height - 1), 2 ** curr_height):
        seg_tree[i] = max(seg_tree[i * 2], seg_tree[i * 2 + 1])
    curr_height -= 1

def seg_query(tree, start, end):
    ans = 0
    while start <= end:
        if start % 2 and tree[start] > ans:
            ans = tree[start]
        if end % 2 == 0 and tree[end] > ans:
            ans = tree[end]
        start = (start + 1) // 2
        end = (end - 1) // 2
    return ans

ans = []
for i in range(m - 1, n - m + 1):
    start = 2 ** (seg_height - 1) + (i - (m - 1))
    end = 2 ** (seg_height - 1) + (i + (m - 1))
    ans.append(seg_query(seg_tree, start, end))
print(*ans)
