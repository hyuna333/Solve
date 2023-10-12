import sys
input = sys.stdin.readline

N, M = map(int, input().split())
namedct = numdct = {}

for i in range(1, N+1):
    name = input().strip()
    namedct[name] = i
    numdct[i] = name

for _ in range(M):
    pokemon = input().strip()

    if pokemon.isnumeric():
        print(numdct[int(pokemon)])
    else:
        print(namedct[pokemon])