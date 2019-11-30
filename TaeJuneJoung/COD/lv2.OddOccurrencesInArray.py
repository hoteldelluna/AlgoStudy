"""
무조건 하나만 홀수가 발생하니
마지막 index는 짝수일 수밖에 없다.(0부터 시작이니)

[조건]
1. A의 크기가 1인 경우
2. 홀수가 중간에 있는 경우
3. 홀수가 맨 마지막에 있는 경우
"""

def solution(A):
    A.sort()
    
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i+1]:
            # 조건2 - 홀수가 1개밖에 없으니 답이 아니라면 짝수개이므로 앞에 것이 틀리다.
            return A[i]
    # 조건1, 3 - 조건2에서 끝나지 않았다면 맨 마지막 값이 답
    return A[-1]


"""
[처음 풀이]
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