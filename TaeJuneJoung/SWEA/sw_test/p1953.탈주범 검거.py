"""
[BFS]
BFS로 퍼져 나가며 모양에 맞는 것을 연결.
갈 수 있는 방향을 가면서 cnt를 +1
"""

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

#상, 우, 하, 좌
move_terminal = [
	[], #0
	[(1,2,5,6), (1,3,6,7), (1,2,4,7), (1,3,4,5)], #1
	[(1,2,5,6), (), (1,2,4,7), ()], #2
	[(), (1,3,6,7), (), (1,3,4,5)], #3
	[(1,2,5,6), (1,3,6,7), (), ()], #4
	[(), (1,3,6,7), (1,2,4,7), ()], #5
	[(), (), (1,2,4,7), (1,3,4,5)], #6
	[(1,2,5,6), (), (), (1,3,4,5)] #7
]

def bfs(y, x, d, cnt):
    q = [(y, x, d)]
    while q:
        lenQ = len(q)
        cnt += 1
        if cnt > L:
            return
        for c in range(lenQ):
            y, x, d = q.pop(0)
            for i in range(len(di)):
                dy = y + di[i]
                dx = x + dj[i]
                if 0 <= dy < N and 0 <= dx < M:
                    if visited[dy][dx] == 0 and arr[dy][dx] > 0:
                        if arr[dy][dx] in set(move_terminal[d][i]):
                            visited[dy][dx] = cnt
                            q.append((dy, dx, arr[dy][dx]))
						

T = int(input())
for t in range(1, 1+T):
	# N:세로 M:가로 R:맨홀 세로 C:맨홀 가로 L:탈출 소요시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    visited[R][C] = 1
    bfs(R, C, arr[R][C], 1)

    cnt_count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                cnt_count += 1

    print(f'#{t} {cnt_count}')
    