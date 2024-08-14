transform = [None, {'d':'q', 'b':'p', 'q':'d','p':'b'}, {'d':'b', 'b':'d', 'q':'p', 'p':'q'}]

n, d =  map(int, input().split())
for _ in range(n):
    s = input()
    ans = ''
    for ch in s:
        ans += transform[d][ch]
    print(ans)