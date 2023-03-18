import sys

dct = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,
       'D+':1.5, 'D0':1.0, 'F':0.0}

sm = i = 0
for _ in range(20):
    lst = list(sys.stdin.readline().split())
    if lst[2] != 'P':
        sm += float(lst[1])*dct[lst[2]]
        i += float(lst[1])

print(sm/i)