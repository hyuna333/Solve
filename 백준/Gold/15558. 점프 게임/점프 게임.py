import sys
input = sys.stdin.readline

N, k = map(int, input().split())
lst = [list(input().strip()) for _ in range(2)]

def jump():
    q = [(0, 0, 0)]
    vi = [[0]*N for _ in range(2)]
    vi[0][0] = 1
    while q:
        line, idx, t = q.pop(0)
        if idx >= N-1 or idx + k > N-1:
            print(1)
            return

        # 할 수 있는거
        if lst[line][idx+1] == '1' and not vi[line][idx+1]:
            q.append((line, idx+1, t+1))
            vi[line][idx + 1] = 1
        if idx-1 >= 0 and lst[line][idx-1] == '1' and idx-1 > t and not vi[line][idx-1]:
            q.append((line, idx-1, t+1))
            vi[line][idx - 1] = 1
        if lst[(line + 1) % 2][idx+k] == '1' and not vi[(line + 1) % 2][idx+k]:
            q.append(((line + 1) % 2, idx+k, t+1))
            vi[(line + 1) % 2][idx + k] = 1

    print(0)

jump()