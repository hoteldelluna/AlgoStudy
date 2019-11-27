# Codility
# Lesson 6 Triangle
'''
리스트 A가 있을때
숫자 세개를 뽑아 

0<= p < q < r < N
A[p] + A[q] > A[r]
A[q] + A[r] > A[p]
A[r] + A[p] > A[q]

위의 조건을 만족하면 1
아니면 0 출력
'''
# Performance tests 는 꽝임
# O(N**3)

# import itertools

# def solution(A):
#     nums_list = itertools.combinations(A, 3)
#     for nums in nums_list:
#         if nums[0] + nums[1] > nums[2]:
#             if nums[1] + nums[2] > nums[0]:
#                 if nums[2] + nums[0] > nums[1]:
#                     return 1
#     return 0


# 방법 2 성공!!
# O(N*log(N))
'''
오름차순 정렬
a, b, c, ... 있을때
a+b 가 c보다 작으면 pass
크면 다른 조건이 맞는지 확인
맞으면 1 출력
아니면 pass
for문 다 돌았는데도 않끝나면 0 출력
'''

def solution(A):
    A.sort()
    N = len(A)
    for i in range(N-2):
        if A[i] + A[i+1] > A[i+2]:
            if A[i+1] + A[i+2] > A[i] and A[i+2] + A[i] > A[i+1]:
                return 1
    return 0 
            

A = [10, 2, 5, 1, 8, 20]
res = solution(A)
print(res)
