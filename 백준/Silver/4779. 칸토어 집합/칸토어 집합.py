import sys

def change(l):
    if l == 1:
        return '-'

    return change(l//3) + (' '*(l//3)) + change(l//3)

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    N = int(line)

    ans = change(3**N)
    print(ans)