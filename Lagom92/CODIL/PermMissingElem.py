# codility PermMissingElem
# lesson 3 - 2
# 리스트 중 없는 숫자 찾기
'''
숫자 하나가 빈 A대신 정답으로 사용할 res 리스트를 하나 만들어서 비교했다.

A의 맨 마지막이 찾는 숫자일 경우가 있으므로
for문 중에 못찾으면 마지막을 return 해줬다.
'''

def solution(A):
    A = sorted(A)
    n = len(A)
    res = [i for i in range(1, n+2)]
    
    for i in range(n):
        if A[i] != res[i]:
            return res[i]
    return res[-1]

result = solution([2, 3, 1])
print(result)