import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

ops = []
symbols = ['+', '-', '*', '/']

for i in range(4):
    ops.extend([symbols[i]] * op[i])
op_permutations = set(permutations(ops))


def postfix(nums, ops):
    pri = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    s = []

    for i in range(len(ops)):
        output.append(str(nums[i]))
        while s and pri[s[-1]] >= pri[ops[i]]:
            output.append(s.pop())
        s.append(ops[i])
    output.append(str(nums[-1]))
    while s:
        output.append(s.pop())

    return output

def evaluate(postfix):
    stack = []
    for token in postfix:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if a < 0:
                    stack.append(-(-a // b))
                else:
                    stack.append(a // b)
    return stack[0]

results = []
for ops in op_permutations:
    tmp = postfix(nums, ops)
    result = evaluate(tmp)
    results.append(result)

print(max(results))
print(min(results))