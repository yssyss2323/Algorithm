import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int,input().split())
pokemons = [None]
pokemons_dic = dict()
for i in range(1, N + 1):
    pokemone = input()
    pokemons.append(pokemone)
    pokemons_dic[pokemone] = i

for _ in range(M):
    test = input()
    if test[0] in '1234567890':
        print(pokemons[int(test)])
    else:
        print(pokemons_dic[test])