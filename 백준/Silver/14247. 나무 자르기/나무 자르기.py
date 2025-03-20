import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split()))
grow = list(map(int, input().split()))
tree = []
for i in range(n):
    tree.append((first[i], grow[i]))

tree.sort(key=lambda x: -x[1])

ans = 0
for base, l in tree:
    ans += base + l * (n-1)
    n -= 1

print(ans)