"""
O(N) or O(N * log(N))의 시간복잡도

초기 문제는 `maxA = max(A)+1`로 하여
visited를 maxA크기만큼 만들어주고 방문 처리 후,
list.index를 이용하여 return하는 방식으로 처리했다.

이번 풀이에서는 자원이 충분하다면,
visited를 다 만들어놓고 접근한다면 시간 복잡도가 덜하지 않을까하여
만들어봤는데 두 결과의 시간복잡도는 동일했다.
max를 사용하는 것도 O(N)의 시간복잡도라 그런 것 같다.
"""


def solution(A):
    visited = [0] * 1000001 #백만
    visited[0] = 1
    for a in A:
        if a > 0:
            visited[a] += 1
    for i in range(len(visited)):
        if visited[i] and visited[i+1] == 0:
            return i+1