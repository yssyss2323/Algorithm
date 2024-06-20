import sys

input = sys.stdin.readline

# 반올림함수 정의 : 파이썬에 내장함수있긴한데 좀 이상함
def my_round(n):
    tmp1 = n * 10000
    tmp2 = int(tmp1)
    if tmp1 - tmp2 >= 0.5:
        tmp2 += 1
    return tmp2 / 10000


# 입력받기 : 종료조건이 따로 없어서 잡기술 사용
trees = dict()
total_num = 0
while True:
    tree = input().strip()
    if not tree:
        break
    trees[tree] = trees.get(tree, 0) + 1
    total_num += 1

# 정답 출력
for tree in sorted(trees.keys()):
    tmp = 100 * trees[tree] / total_num
    #percent = my_round(tmp)
    print(f"{tree} {tmp:.4f}")
