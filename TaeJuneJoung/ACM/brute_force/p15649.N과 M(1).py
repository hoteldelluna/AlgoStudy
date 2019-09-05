"""
[완전탐색_순열]
"""

def f(n,k,m):
    if(n==m):
        print(*res)
        return
    else:
        for i in range(k):
            if(visited[i]==0):
                visited[i] = 1
                res[n] = arr[i]
                f(n+1,k,m)
                visited[i] = 0

# k = 자리수
# m = 길이
k, m = map(int, input().split())
arr = range(1,k+1)
res = [0] * m
visited = [0 for i in range(k)]
f(0,k,m)