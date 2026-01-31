check = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9
}

ans = (check[input()] * 10 + check[input()]) * 10 ** check[input()]
print(ans)