"""
[네트워크]
풀다가 다른 사람 소스 확인함
"""

def solution(n, computers):
    visited = [0] * n
    answer = 0
    def dfs(compouters, visited, start):
        stack = [start]
        while stack:
            x = stack.pop()
            if visited[x] == 0:
                visited[x] = 1
                for i in range(n):
                    if computers[x][i] == 1 and visited[i] == 0:
                        stack.append(i)
    idx = 0
    while 0 in set(visited):
        if visited[idx] == 0:
            dfs(computers, visited, idx)
            answer += 1
        idx += 1
    return answer