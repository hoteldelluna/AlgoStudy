"""
index도 시간복잡도는 O(n)
현재 코드의 시간복잡도는 O(N) or O(N * log(N))
"""

def solution(A):
    visited = [0] * (len(A)+2)
    visited[0] = 1
    for a in A:
        visited[a] = 1
    return visited.index(0)

"""
다른 풀이1)
순차적으로 1부터~N까지이니,
N+1까지 더해준 값에서 A의 합을 빼주면 빠진 값이 나온다.

def solution(A):
    return sum(range(1,len(A)+2)) - sum(A)

위의 로직을 보다 더 효율적으로 만들어볼때,
sum = N(N+1)/2
def solution(A):
    return (len(A)+1)*(len(A)+2)//2 - sum(A)
"""