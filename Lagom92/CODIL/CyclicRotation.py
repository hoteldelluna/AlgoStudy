# codility CyclicRotation
# lesson 2 - 2
# A 리스트의 값을 K번 회전 시키기
'''
조건은 잘 걸어주는게 중요하다
아무것도 없거나
한번도 회전을 안시키거나
제자리 걸음을 할때를 제외시켜야 한다.

가장 중요!
뒤에서 앞으로 회전이 된다!!!
'''

def solution(A, K):
    N = len(A)
    
    if N == 0:
        return []
    elif N == K or K == 0 or K % N == 0:
        return A
    else:
        cnt = K % N
        # print("cnt: {}".format(cnt))
        a, b = A[:N-cnt], A[N-cnt:]
        # print(a, b)
        res = b + a
        return res

print(solution(A, K))