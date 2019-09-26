"""
배열의 길이만큼 돌면은 원상태이므로,
나머지값으로 처리

뒤에서 앞으로 옮겨주는 것이므로 -인덱스 활용
"""

def solution(A, K):
    if len(A):
        K = K%len(A)
        ans = A[-K:] + A[:-K] if K else A
        return ans
    else:
        return A