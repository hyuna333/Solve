A, B = map(int, input().split())
C = int(input())

if B+C >= 60:
    A = (A+(B+C)//60)%24
    B = (B+C)%60
elif B+C < 60:
    B += C

print(A, B)