import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    order = input()
    n = int(input())
    numlist = list(input()[1:-1].split(','))
    Rcount = 0 # R 개수 카운팅
    D_even_odd = [0, 0] # 각 D에 대해 앞선 R개수가 짝수인 경우와 홀수인 경우를 저장
    for chr in order:
        if chr == 'R':
            Rcount += 1
        else: # 'D'
            if Rcount % 2 == 0:
                D_even_odd[0] += 1
            else:
                D_even_odd[1] += 1
    if len(order) - Rcount > n:
        print('error')
    else:
        answerlist = numlist[D_even_odd[0]:n - D_even_odd[1]]
        if Rcount % 2 == 1:
            answerlist.reverse()
        print(f"[{','.join(answerlist)}]")