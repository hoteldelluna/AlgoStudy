# Codility
# Lesson 9 MaxProfit
'''
리스트 A의 길이가 0일 경우를 생각해야함
최소에서 사서 최대일때 판다(profit 발생)


나중에 한번 더 풀어보면 좋겠다!!
'''
# 방법 1
def solution(A):
    profit = 0
    N = len(A)
    if N < 1:
        return 0
    minV = A[0]
    for i in range(1, N):
        profit = max(profit, A[i]-minV)
        minV = min(minV, A[i])

    return profit

# 방법 2
# try문을 사용해 보고 싶어서 아래처럼 변경해 봤음
def solution(A):
    N = len(A)
    try:
        minV = A[0]
        profit = 0
        for i in range(1, N):
            profit = max(profit, A[i]-minV)
            minV = min(minV, A[i])
        return profit
    except:
        return 0