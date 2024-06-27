t = int(input())
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print(f"1 {len(s)//2 + 1}")
    else:
        ncall = 1
        for i in range(len(s) // 2):
            if s[i] == s[len(s) - 1 - i]:
                ncall += 1
            else:
                break
        print(f"0 {ncall}")