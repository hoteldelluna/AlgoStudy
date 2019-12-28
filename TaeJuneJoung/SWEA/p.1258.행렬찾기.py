"""
[p1258.[S/W 문제해결 응용] 7일차 - 행렬찾기]

"""

def bfs(i,j, arr):
    q = [(i,j)]
    point = [1, 1]
    while q:
        y, x = q.pop()
        if y < N-1 and x < N-1:
            if arr[y][x+1] != 0:
                point[1] += 1
                arr[y][x+1] = 0
                q.append([y, x+1])
            elif arr[y+1][x] != 0:
                point[0] += 1
                arr[y+1][x] = 0
                q.append([y+1, x])
        elif x == N-1:
            if arr[y+1][x] != 0:
                point[0] += 1
                arr[y+1][x] = 0
                q.append([y+1, x])
    for di in range(i, y+1):
        for dj in range(j, x+1):
            arr[di][dj] = 0
    return point


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    box = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                arr[i][j] = 0
                cnt += 1
                box.append(bfs(i,j, arr))
    
    box.sort(key=lambda x: (x[0] * x[1], x[0]))
    res = ''
    for i in range(len(box)):
        if i == len(box)-1:
            res += str(box[i][0]) + ' ' + str(box[i][1])
        else:
            res += str(box[i][0]) + ' ' + str(box[i][1]) + ' '
    print(f'#{t} {cnt} {res}')
