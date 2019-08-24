"""[BFS/DFS]
1이 있는지 검사하며 방문 했다면 해당 배열을 0으로 처리해주거나,
방문 배열에 방문했다고 표시한 후, 방문 한 곳은 다시 가지 않게 처리해준다.
1이 있어서 방문한 총 개수를 출력하면 완성

DFS로도 풀어보기
"""

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, cnt):
    q = []
    q.append(i)
    q.append(j)
    cnt += 1
    while q:
        i = q.pop(0)
        j = q.pop(0)
        for k in range(4):
            dx = i + di[k]
            dy = j + dj[k]
            if 0 <= dx < N and 0 <= dy < M:
                if arr[dx][dy] == 1 and visited[dx][dy] == 0:
                    cnt += 1
                    visited[dx][dy] = 1
                    q.append(dx)
                    q.append(dy)
    return cnt


# M:가로길이 N:세로길이 K:배추 위치 개수
T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())

    arr = [[0]*M for i in range(N)]
    visited = [[0]*M for i in range(N)]

    cnt_list = []
    for i in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1

    cnt = 0
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j, cnt)
                res += 1
    print(res)