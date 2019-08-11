"""[BFS/DFS]
그래프의 경로이며 가중치가 1이기에
BFS와 DFS 둘다 풀 수 있음
화살표를 보면 단방향임을 알 수 있다.
"""

#[BFS]
def bfs(start, graph):
    visited[start] = 1
    q = []
    q.append(start)
    graph.append(start)
    while q:
        start = q.pop(0)
        if start >= 0 and start < V+1:
            for i in range(1, V+1):
                if matrix[start][i] == 1 and visited[i] != 1:
                    visited[i] = 1
                    q.append(i)
                    graph.append(i)
    return graph

T = int(input())
for t in range(1, T+1):
    stack = []
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for i in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        a, b = map(int, input().split())
        matrix[a][b] = 1
    
    start, end = map(int, input().split())
    graph = []
    if end in bfs(start, graph):
        res = 1
    else:
        res = 0
    
    print("#{} {}".format(t, res))

#[DFS]
def dfs(start):
    visited[start] = 1
    stack.append(start)
    for i in range(1, V+1):
        if matrix[start][i] == 1 and visited[i] != 1:
            visited[i] = 1
            dfs(i)
    return stack

T = int(input())
for t in range(1, T+1):
    stack = []
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for i in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        a, b = map(int, input().split())
        matrix[a][b] = 1
    
    start, end = map(int, input().split())
    if end in dfs(start):
        res = 1
    else:
        res = 0
    print("#{} {}".format(t, res))