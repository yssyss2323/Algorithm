n = int(input())
game_result = list(map(int,input().split()))
original = []
while game_result:
    for i in range(len(game_result)):
        tmp = game_result[i]
        if tmp * 2 not in game_result and (tmp % 3 != 0 or tmp // 3 not in game_result):
            original.append(tmp)
            del game_result[i]
            break
print(*original[::-1])