"""
[완전탐색_순열]
"""

def f(n,k,m):
    if(n==m):
        print(*res)
        return
    else:
        for i in range(k):
            res[n] = arr[i]
            f(n+1,k,m)

# k = 자리수
# m = 길이
k, m = map(int, input().split())
arr = range(1,k+1)
res = [0] * m
f(0,k,m)