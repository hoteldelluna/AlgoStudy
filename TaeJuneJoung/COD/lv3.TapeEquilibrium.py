def solution(A):
    minV = 9876543210
    left, right = 0, sum(A)
    for i in range(len(A)-1):
        left += A[i]
        right -= A[i]
        value = abs(left - right)
        minV = value if value < minV else minV
    return minV