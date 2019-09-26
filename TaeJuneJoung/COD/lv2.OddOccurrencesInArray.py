"""
시도를 해본 문제
문제를 이해를 잘못한 부분도 한몫하였고,
효율성을 가장 크게 생각해야했던 문제

처음에는 set으로 감싸서 중복을 없앤 후,
해당 set내용으로 A.count를 하였으나 N^2이 나와 실패

Dict형태도 퍼포먼스에서는 좋지 않았다.

어떻게 짜면 효율적일지 다른 방도로 생각해보면 좋을듯한 문제.

현재 방법은 100점이나, 더 좋은 방도가 없을까?
"""

def solution(A):
    A.sort()
    if len(A) < 2:
        return A[0]
    cnt = 1
    for i in range(1, len(A)):
        if A[i-1] == A[i]:
            cnt += 1
        else:
            if cnt%2:
                return A[i-1]
            else:
                cnt = 1
    return A[i]