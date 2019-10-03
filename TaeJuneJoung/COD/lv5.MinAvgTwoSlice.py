"""
시간복잡도가 O(N)이 나와야 퍼포먼스가 통과할텐데...
우선은 O(N^2^)밖에 생각 안나니 먼저 짜본다.

#시간복잡도 O(N^2^)
def solution(A):
    idx = 0
    minV = 20001
    for i in range(len(A)-1):
        val = A[i]
        n = 1
        for j in range(i+1,len(A)):
            val += A[j]
            n += 1
            avg_val = val / n
            if avg_val < minV:
                idx = i
                minV = avg_val
    return idx


이 문제를 빠르게 풀기 위해선 두 가지 규칙을 생각해보아야 한다.
1. 평균은 '평균의 평균'이라는 것이다.
    [1,2,3,4]라는 A가 있다고 할 때,
    [1,2]의 평균 = 1.5
    [3,4]의 평균 = 3.5
    [1,2,3,4]의 평균 = 2.5이며 (1.5+3.5)/2와 같다.

2. 평균은 가장 작은 인자보다 항상 크다.

이 두가지를 보았을 때, 우리는 리스트가 4이상일 경우는 확인하지 않아도 된다.
길이가 3인 경우를 판단하는 이유는,
2개의 부분집합으로는 3개의 부분집합을 구할 수 없기 때문이다.

참조) https://huy0502.tistory.com/19
"""


def solution(A):
    idx = 0
    minV = 20001
    for i in range(len(A)):
        if i + 1 < len(A):
            val = (A[i] + A[i+1]) / 2
            if val < minV:
                minV = val
                idx = i
        
        if i + 2 < len(A):
            val = (A[i] + A[i+1] + A[i+2]) / 3
            if val < minV:
                minV = val
                idx = i
        
    return idx