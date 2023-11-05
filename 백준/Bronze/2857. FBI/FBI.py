import sys
input = sys.stdin.readline

ans = []
for j in range(5):
    name = input()
    l = len(name)
    for i in range(l-2):
        if name[i] == 'F':
            if name[i+1] == 'B':
                if name[i+2] == 'I':
                    ans.append(j+1)
                    break

if not ans:
    print("HE GOT AWAY!")
else:
    print(*ans)