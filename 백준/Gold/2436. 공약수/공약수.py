def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


a, b = map(int, input().split())
total = b // a # total은 서로소인 두 수의 곱이 될 것임
candidates = [i for i in range(int(total ** 0.5), 0, -1) if total % i == 0] # 두 수 후보들
for candidate1 in candidates:
    candidate2 = total // candidate1
    if gcd(candidate1, candidate2) == 1: # 두 수가 서로소 -> 조건 충족
        print(a * candidate1, a * candidate2)
        break
