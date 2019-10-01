"""
기존에 풀던 방식이 퍼포먼스가 좋지 않아서 다른 사람 코드를 참조한 소스
O(N+M)의 시간복잡도를 가진다.
"""

def solution(N, A):
    visited = [0] * N
    preMax = 0
    maxV = 0
    for a in A:
        if a > N:
            maxV = preMax
        else:
            if maxV > visited[a-1]:
                visited[a-1] = maxV
            
            visited[a-1] += 1

            if preMax < visited[a-1]:
                preMax = visited[a-1]

    for i in range(N):
        if visited[i] < maxV:
            visited = maxV
            
    return visited