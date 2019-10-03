"""
시간복잡도: O(N * log(N))
보너스 문제 같은 느낌이지만,
sort를 직접 짤 수 있어야 진짜 푼 느낌일거 같은 문제
"""

def solution(A):
    A.sort()
    back = A[0] * A[1] * A[-1]
    front = A[-1] * A[-2] * A[-3]
    maxV = back if back > front else front
    return maxV