def solution(n, left, right):
    answer = []
    leftn, leftm = left // n, left % n
    rightn, rightm = right // n, right % n
    first = [leftn+1]*leftn + [x for x in range(leftn+1,n+1)]
    if leftn == rightn:
        answer = first[leftm:rightm+1]
    else:
        answer += first[leftm:]
        for i in range(leftn+1, rightn):
            tmp = [i+1] * i + [x for x in range(i+1,n+1)]
            answer += tmp
        last = [rightn+1]*rightn + [x for x in range(rightn+1,n+1)]
        answer += last[:rightm+1]
    return answer