# Codility
# Lesson 6 Distinct
'''
리스트 A가 주어질때
중복을 제거
갯수 출력
'''

def solution(A):
    # print(A)
    A_set = set(A)
    # print(A_set)
    return len(A_set)
