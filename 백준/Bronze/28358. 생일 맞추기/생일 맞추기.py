import sys
input = sys.stdin.readline

for _ in range(int(input())):
    check = list(map(int, input().split()))
    days = [True for _ in range(31)]
    months = [True for _ in range(12)]
    day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    last_day = {'29': 0, '30': 0, '31': 0}
    for i in range(10):
        if check[i] == 1:
            for j in range(1, 32):
                if str(i) in str(j):
                    days[j - 1] = False
            for j in range(1, 13):
                if str(i) in str(j):
                    months[j - 1] = False
    last_day['29'] = days[:29].count(True)
    last_day['30'] = days[:30].count(True)
    last_day['31'] = days[:31].count(True)
    ans = 0
    for i in range(12):
        if months[i]:
            ans += last_day[str(day_in_month[i])]
    print(ans)
