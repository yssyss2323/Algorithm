t = int(input())
for i in range(t):
    n = int(input())
    strings = input()
    ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(strings) == 1:
        ans = "IMPOSSIBLE"
    else:
        if strings in ans:
            idx = ans.find(strings)
            ans = ans[:idx] + strings[::-1] + ans[idx+len(strings):]
    print(f"Case #{i+1}: {ans}")
