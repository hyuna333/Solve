import sys

N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    st = sys.stdin.readline().strip()
    if st.isalpha():
        if st == 'pop':
            if lst:
                print(lst.pop())
            else:
                print(-1)
        elif st == 'size':
            print(len(lst))
        elif st == 'empty':
            if lst:
                print(0)
            else:
                print(1)
        elif st == 'top':
            if lst:
                print(lst[-1])
            else:
                print(-1)
    else:
        a, b = st.split()
        lst.append(int(b))