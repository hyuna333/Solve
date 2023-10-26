import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 프린터기 중요도 순서
    ipt = list(map(int, input().split()))
    # 내가 찾아야하는 문서의 중요도와 위치
    doc = ipt[M]
    po = M
    # 지금까지 프린트 된 문서의 수
    ans = 0

    while ipt:
        mx = max(ipt)
        tmp = ipt.pop(0)
        if tmp == mx:
            ans += 1
            if tmp == doc and po == 0:
                break
            po -= 1
        else:
            if po == 0:
                po = len(ipt)
            else:
                po -= 1
            ipt.append(tmp)

    print(ans)