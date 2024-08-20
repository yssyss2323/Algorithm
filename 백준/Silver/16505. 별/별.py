def star(n):
    if n == 0:
        return ['*']
    arr1, arr2 = [], []
    for ch in star(n - 1):
        arr1.append(ch + ' ' * (2 ** (n - 1) - len(ch)) + ch)
        arr2.append(ch)
    return arr1 + arr2

n = int(input())
for ch in star(n):
    print(ch)