import sys
input = sys.stdin.readline

while True:
    member = list(input().split())

    if member[0] == "#":
        break

    if int(member[1]) > 17 or int(member[2]) >= 80:
        print(member[0], "Senior")
    else:
        print(member[0], "Junior")