import sys


def solve():
    # 입력 받기
    # A, B, C: 직선 방정식 Ax + By + C = 0 의 계수
    A, B, C = map(int, sys.stdin.readline().split())

    # X1, X2, Y1, Y2: 직사각형의 범위
    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())

    # 직사각형의 네 꼭짓점 좌표
    # (x1, y1), (x2, y1), (x2, y2), (x1, y2)

    # 직선의 방정식 함수 f(x, y) = Ax + By + C
    def f(x, y):
        return A * x + B * y + C

    # 네 꼭짓점에 대해 대입한 결과 계산
    res1 = f(x1, y1)
    res2 = f(x2, y1)
    res3 = f(x2, y2)
    res4 = f(x1, y2)

    # 4개의 결과값 리스트
    results = [res1, res2, res3, res4]

    # 최댓값과 최솟값 구하기
    max_val = max(results)
    min_val = min(results)

    # 판별 로직
    # 내부를 지나려면, 직선을 기준으로 한쪽에는 양수, 반대쪽에는 음수인 점이 반드시 있어야 함.
    # 즉, 최댓값은 0보다 크고, 최솟값은 0보다 작아야 함.
    if max_val > 0 and min_val < 0:
        print("Poor")
    else:
        # 모두 양수거나, 모두 음수거나, 0이 포함되어 있어도 부호가 엇갈리지 않는 경우 (접하거나 테두리)
        print("Lucky")


if __name__ == "__main__":
    solve()