# Codility PermCheck

'''
순서대로 리스트를 정렬했을때 
빠진 숫자가 있으면 0을 출력
없으면 1을 출력
'''

def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(len(A)):
        if i+1 == A[i]:
            pass
        else:
            return 0
    return 1