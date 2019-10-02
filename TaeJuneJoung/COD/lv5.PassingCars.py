"""
Prefix sums을 생각해보면 풀리는 문제
처음에는 2중 for문을 사용하여 풀면 O(N^2^)이 나온다.
"""

def solution(A):
    cnt = 0
    answer = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 1:
            cnt += 1
        else:
            answer += cnt
            
    if answer > 1000000000:
        return -1
    return answer