import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    min_heap, max_heap = [], []
    visited = {}

    k = int(input())
    for _ in range(k):
        operation, num = input().split()
        num = int(num)

        if operation == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            visited[num] = visited.get(num, 0) + 1
        else:
            if num == 1:
                while max_heap and visited[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
            elif num == -1:
                while min_heap and visited[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0]] -= 1
                    heapq.heappop(min_heap)

    while min_heap and visited[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and visited[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])