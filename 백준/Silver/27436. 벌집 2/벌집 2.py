n=int(input())
m=int(((n-1)/3)**0.5)
print(m+2 if n>1+3*m*(m+1) else m+1)