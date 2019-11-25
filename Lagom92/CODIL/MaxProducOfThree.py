# Codility
# Lesson 6 Sorting
# MaxProductOfThree
'''
주어진 리스트의 숫자 중 3개를 뽑아 곱했을때
최대값을 구하는 문제

itertools의 combinations를 사용했다.
'''
# 시간 초과 발생..ㅜ

# import itertools

# def solution(A):
#     maxV = -10000
#     res = list(itertools.combinations(A, 3))
#     print(res)
    
#     for nums in res:
#         val = nums[0] * nums[1] * nums[2]
#         if maxV < val:
#             maxV = val
#             print(nums)
#     return maxV

'''
호근형의 아이디어로 해결!
'''
def solution(A):
    A.sort()
    numA = A[0] * A[1] * A[-1]
    numB = A[-1] * A[-2] * A[-3]
    
    if numA > numB:
        return numA
    else:
        return numB

N = [-3, 1, 2, -2, 5, 6]
result = solution(N)
print(result)

