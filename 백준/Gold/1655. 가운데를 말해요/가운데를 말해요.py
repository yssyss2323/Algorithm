# def cnt(x, y):
#     return x + y - 1
#
# def find_square(x):
#     squares = []
#     for i in range(3, x//2):
#         check = x ** 2 - i ** 2
#         if check ** 0.5 == int(check ** 0.5):
#             squares.append((i, int(check ** 0.5)))
#     return squares
#
# n = int(input())
# print(find_square(n // 2))
import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = [-int(input())]
min_heap = []
print(-max_heap[0])
for _ in range(n - 1):
    curr = int(input())
    if len(max_heap) == len(min_heap):
        if min_heap[0] >= curr:
            heapq.heappush(max_heap, -curr)
        else:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, curr)
    else:
        if -max_heap[0] < curr:
            heapq.heappush(min_heap, curr)
        else:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -curr)
    print(-max_heap[0])