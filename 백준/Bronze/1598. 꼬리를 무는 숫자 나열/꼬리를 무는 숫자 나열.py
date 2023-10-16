import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ai, aj = (N - 1) // 4, (N - 1) % 4
bi, bj = (K - 1) // 4, (K - 1) % 4

ans = abs(ai - bi) + abs(aj - bj)

print(ans)