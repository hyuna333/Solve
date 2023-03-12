T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    P = ''
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'

    for i in range(len(S)):
        if S[i] in alpha:
            P += S[i]*R

    print(P)