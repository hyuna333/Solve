import sys

N = int(sys.stdin.readline())

lst = []

for _ in range(N):
    st = str(sys.stdin.readline().rstrip())
    lst.append(st)

lst = list(set(lst))

lst.sort()
lst.sort(key= lambda x : (len(x), x))

print(*lst, sep='\n')