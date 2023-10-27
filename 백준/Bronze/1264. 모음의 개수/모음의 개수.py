import sys
input = sys.stdin.readline

while True:
    st = input().strip().lower()
    if st == '#':
        break
    else:
        ans = 0
        for alp in ('a', 'e', 'i', 'o', 'u'):
            ans += st.count(alp)
        print(ans)