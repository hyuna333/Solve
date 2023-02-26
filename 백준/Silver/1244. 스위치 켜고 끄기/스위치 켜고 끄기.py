import sys

N = int(sys.stdin.readline())
sw = [0]+list(map(int, sys.stdin.readline().split()))
stu = int(sys.stdin.readline())

for _ in range(stu):
    gen, num = map(int, sys.stdin.readline().split())
    # 남자일때
    if gen == 1:
        for i in range(1, N+1):
            # 배수라면 0<>1 바꿔주기
            if i%num == 0:
                sw[i] = (sw[i]+1)%2
    # 여자일때
    else:
        # 받은 자리 바꿔주고
        sw[num] = (sw[num] + 1) % 2
        # 받은 자리가 스위치의 중간부분보다 크다면
        if num > N//2:
            # 스위치길이-받은 자리를 범위로 대칭인지 확인 후 대칭이면 0<>1 바꿔주고 아니라면 멈춤
            for i in range(1, N-num+1):
                if sw[num-i] == sw[num+i]:
                    sw[num-i], sw[num+i] = (sw[num-i] + 1) % 2, (sw[num+i] + 1) % 2
                else:
                    break
        # 받은 자리가 스위치의 중간부분부다 작다면
        else:
            # 받은 자리를 범위로 대칭인지 확인 후 대칭이면 0<>1 바꿔주고 아니라면 멈춤
            for i in range(1, num):
                if sw[num-i] == sw[num+i]:
                    sw[num-i], sw[num+i] = (sw[num-i] + 1) % 2, (sw[num+i] + 1) % 2
                else:
                    break

# 20개씩 끊어주기
for i in range(1, len(sw), 20):
    ans = sw[i:i+20]
    print(*ans)

