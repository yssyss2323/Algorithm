b, c, d = map(int, input().split())
t = min(b, c, d)

burger_price = sorted(map(int, input().split()))
side_price = sorted(map(int, input().split()))
drink_price = sorted(map(int, input().split()))

discount = int((sum(burger_price[-t:]) + sum(side_price[-t:]) + sum(drink_price[-t:])) * 0.1)
tot_price = sum(burger_price) + sum(side_price) + sum(drink_price)
print(tot_price)
print(tot_price - discount)