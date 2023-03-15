N = input()

for i in range(len(N)//2):
    if N[i] != N[-1-i]:
        print(0)
        break
else:
    print(1)