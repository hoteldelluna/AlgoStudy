"""
[완전탐색_재귀]
p14888의 문제 풀이와 동일
"""

def f(s, idx, plus, minus, mul, div):
    global minV, maxV
    if idx >= N:
        minV = s if s < minV else minV
        maxV = s if s > maxV else maxV
    else:
        if plus: f(s+M[idx], idx+1, plus-1, minus, mul, div)
        if minus: f(s-M[idx], idx+1, plus, minus-1, mul, div)
        if mul: f(s*M[idx], idx+1, plus, minus, mul-1, div)
        if div: f(int(s/M[idx]), idx+1, plus, minus, mul, div-1)

N = int(input())
M = list(map(int, input().split()))
C = list(map(int, input().split()))
minV = 987654321
maxV = -987654321

f(M[0], 1, C[0], C[1], C[2], C[3])

print(maxV)
print(minV)