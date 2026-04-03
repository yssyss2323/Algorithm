n = int(input())
string = input()

num_big = string.count("bigdata")
num_sec = string.count("security")

if num_big > num_sec:
    print("bigdata?")
elif num_big < num_sec:
    print("security!")
else:
    print("bigdata? security!")