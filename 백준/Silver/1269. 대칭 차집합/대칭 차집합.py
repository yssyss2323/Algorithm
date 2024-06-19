na, nb = map(int, input().split())
elements_a = set(map(int, input().split()))
elements_b = set(map(int, input().split()))
a_or_b = elements_a.intersection(elements_b)

print(na + nb - 2 * len(a_or_b))