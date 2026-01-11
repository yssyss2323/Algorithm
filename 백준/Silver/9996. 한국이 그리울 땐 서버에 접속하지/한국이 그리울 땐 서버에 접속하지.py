import re
n = int(input())
check = input().replace("*", "[a-z]*") + "$"
for _ in range(n):
    print(['NE',"DA"][bool(re.match(check, input()))])