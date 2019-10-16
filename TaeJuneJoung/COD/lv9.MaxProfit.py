"""
장사꾼이 일자 중에 가장 싼 날에 물건을 사와서,
가장 비싼 날에 물건을 파는 방식

1. 가장 싼 날은 가장 비싼 날 보다 이전 날이어야 한다.
2. 판매 이익이 없다면 return 0을 한다
3. 2번의 규칙에 따르면, 하루만 있다면 이익이 없는 날이다

유사한 문제
SW Expert Academy 1859. 백만 장자 프로젝트
https://github.com/hoteldelluna/AlgoStudy/blob/python/TaeJuneJoung/TaeJuneJoung/SWEA/p1859.%EB%B0%B1%EB%A7%8C%20%EC%9E%A5%EC%9E%90%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8.py
"""

def solution(A):
    if len(A) < 2:
        return 0
    maxSum = 0
    maxV = A[-1]
    for i in range(len(A)-2, -1, -1):
        maxSum = max(maxSum, maxV - A[i])
        maxV = max(maxV, A[i])
    return maxSum