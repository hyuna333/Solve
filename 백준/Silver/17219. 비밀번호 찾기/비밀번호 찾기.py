import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dct = {}

for _ in range(N):
    site, pwd = input().split()
    dct[site] = pwd

for _ in range(M):
    find = input().strip()
    print(dct[find])