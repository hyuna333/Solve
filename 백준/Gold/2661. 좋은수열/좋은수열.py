import sys
input = sys.stdin.readline

N = int(input().strip())
result = ""


def good(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True


def dfs(seq):
    global result
    if result:
        return

    if len(seq) == N:
        result = seq
        return

    for num in '123':
        next_seq = seq + num
        if good(next_seq):
            dfs(next_seq)


dfs("")
print(result)