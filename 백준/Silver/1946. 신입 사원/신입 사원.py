import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    interview_ranks = [0] * n
    for _ in range(n):
        paper_rank, interview_rank = map(lambda x: int(x) - 1, input().split())
        interview_ranks[paper_rank] = interview_rank # paper_rank 순으로 interview_rank 정렬

    cnt = 0
    curr = n
    for i in range(n):
        if curr > interview_ranks[i]:
            curr = interview_ranks[i]
            cnt += 1
    print(cnt)