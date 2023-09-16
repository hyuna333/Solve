import sys
input = sys.stdin.readline

N = int(input())
deck = []

for _ in range(N):
    tmp = list(input().split())

    if tmp[0] == "push_front":
        deck.insert(0, int(tmp[1]))
    elif tmp[0] == "push_back":
        deck.append(int(tmp[1]))
    elif tmp[0] == "pop_front":
        if deck:
            print(deck.pop(0))
        else:
            print(-1)
    elif tmp[0] == "pop_back":
        if deck:
            print(deck.pop(-1))
        else:
            print(-1)
    elif tmp[0] == "size":
        print(len(deck))
    elif tmp[0] == "empty":
        if deck:
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if deck:
            print(deck[-1])
        else:
            print(-1)