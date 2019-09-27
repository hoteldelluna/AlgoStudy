"""
다른 사람들 코드를 보고 참고하여 푼 문제
이해가 너무도 안되는 문제...
"""

def solution(X, A):
    C = [0]* (X+1)
    cnt = 0
    for i in range(len(A)):
        if C[A[i]] == 0:
            C[A[i]] = 1
            cnt += 1
            if cnt == X:
                return i
    return -1