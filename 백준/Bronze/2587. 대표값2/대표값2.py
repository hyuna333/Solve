import sys

sm = 0
lst = []
for _ in range(5):
    N = int(sys.stdin.readline())
    sm += N
    if not lst:
        lst.append(N)
    else:
        for i in range(len(lst)):
            if lst[i] > N:
                lst.insert(i, N)
                break
        else:
            lst.append(N)

avg = sm//5

print(avg)
print(lst[2])