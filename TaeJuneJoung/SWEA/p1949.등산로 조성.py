"""
완전탐색
"""

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def f(i, j, c, k):
    global maxV
    if maxV < c:
        maxV = c
    visited[i][j] = 1
    for d in range(len(di)):
        x = i + di[d]
        y = j + dj[d]
        if 0 <= x < N and 0 <= y < N:
            if visited[x][y] == 0:
                if arr[i][j] > arr[x][y]:
                    f(x, y, c+1, k)
                elif arr[i][j] > arr[x][y] -k:
                    temp = arr[x][y]
                    arr[x][y] = arr[i][j] -1
                    f(x, y, c+1, 0)
                    arr[x][y] = temp

    visited[i][j] = 0

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    high = 0
    for i in range(N):
        high = max(arr[i]) if max(arr[i]) > high else high
    
    maxV = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == high:
                c = 1
                f(i, j, c, K)

    print("#{} {}".format(t, maxV))

