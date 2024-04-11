n = int(input())
sum, i = 0,0
while True:
    i += 1
    sum += i
    if sum -i < n and n<= sum:
        break
if i%2 ==0:
    daughter = n - (i-1)*i//2
else:
    daughter = (i**2+1)-n-(i-1)*i//2
        
mom = i+1 - daughter
print(f"{daughter}/{mom}")