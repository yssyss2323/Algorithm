def ring_my_bell(player1, player2, ground1, ground2):
    # player1 종침
    if (ground1 and ground1[-1] == 5) or (ground2 and ground2[-1] == 5):
        player1.extendleft(ground2)
        player1.extendleft(ground1)
        ground1.clear()
        ground2.clear()

    # player2 종침
    elif ground1 and ground2 and ground1[-1] + ground2[-1] == 5:
        player2.extendleft(ground1)
        player2.extendleft(ground2)
        ground1.clear()
        ground2.clear()

def player_turn(player1, player2, ground1, ground2, n):
    if n % 2 == 0:
        ground1.append(player1.pop())
        if not player1:
            print('su')
            exit()
    else:
        ground2.append(player2.pop())
        if not player2:
            print('do')
            exit()


if __name__ == "__main__":
    from collections import deque
    import sys

    # 입력 받기
    #sys.stdin = open('output.txt', 'r')
    input = sys.stdin.readline
    winner = {1: 'do', 2: 'su', 3: 'dosu'}
    n, m = map(int, input().split())
    do, su = deque(), deque()
    do_ground, su_ground = [], []
    for _ in range(n):
        d, s = map(int, input().split())
        do.append(d)
        su.append(s)

    # 게임진행
    for i in range(m):
        player_turn(do, su, do_ground, su_ground, i)
        ring_my_bell(do, su, do_ground, su_ground)
    # 게임 m판을 모두 진한 경우
    else:
        final_do, final_su = len(do), len(su)
        if final_do > final_su:
            print('do')
        elif final_do < final_su:
            print('su')
        else:
            print('dosu')
