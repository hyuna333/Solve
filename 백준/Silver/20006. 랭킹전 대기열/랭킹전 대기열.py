import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    lv, pl = input().split()
    lv = int(lv)
    if not rooms:
        rooms.append([(lv, pl)])
    else:
        go = False
        for room in rooms:
            if len(room) < m and room[0][0] - 10 <= lv <= room[0][0] + 10:
                room.append((lv, pl))
                go = True
                break
        if not go:
            rooms.append([(lv, pl)])

for ans in rooms:
    ans.sort(key=lambda x : x[1])
    if len(ans) == m:
        print('Started!')
    else:
        print('Waiting!')
    for mem in ans:
        print(*mem)