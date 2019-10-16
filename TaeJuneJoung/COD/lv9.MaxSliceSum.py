"""
[MaxSliceSum]
보통 3중 for문으로 풀 것을 O(N)으로 나오게 푸는 방법
"""

def solution(A):
    maxSum = maxV = A[0]
    for i in range(1, len(A)):
        maxV = max(maxV + A[i], A[i])
        maxSum = max(maxSum, maxV)
    return maxSum