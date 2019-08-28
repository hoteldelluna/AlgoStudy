"""
[완전탐색_순열]
"""

def nPr(r, n, k, x, y):
    if r == k:
        dis = 0
        for i in box:
            X, Y = abs(x - i[0]), abs(y - i[1])
            x, y = i[0], i[1]
            dis += X + Y
        dis += abs(x - WORK[0]) + abs(y - WORK[1])
        res.append(dis)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                box[r] = matrix[i]
                nPr(r+1, n, k, x, y)
                visited[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    matrix = list(map(int, input().split()))
    HOME = [matrix[0], matrix[1]]
    WORK = [matrix[2], matrix[3]]
    matrix = [[matrix[2*i+4], matrix[2*i+5]] for i in range(N)]
    box = [0] * N
    visited = [0] * N
    res = []
    nPr(0, N, N, HOME[0], HOME[1])
    print(f"#{t} {min(res)}")