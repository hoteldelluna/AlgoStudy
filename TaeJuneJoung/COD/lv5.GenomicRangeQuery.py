
"""
#범위를 너무 크게 잡아서 O(N^2^) 시간복잡도로 퍼포먼스 실패
def solution(S, P, Q):
    ACGT = {'A':1, 'C':2, 'G':3, 'T':4}
    ans = [4] * len(P)
    for i in range(len(P)):
        #S[P[i]] ~ S[Q[i]]
        minV = 4
        for j in range(P[i], Q[i]+1):
            if ans[i] > ACGT[S[j]]:
                ans[i] = ACGT[S[j]]
    return ans

아래의 소스는 시간복잡도 O(N + M)을 가지고 있으며,
퍼포먼스 성공!
"""
def solution(S, P, Q):
    V = [0] * len(P)
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            V[i] = 1
        elif 'C' in S[P[i]:Q[i]+1]:
            V[i] = 2
        elif 'G' in S[P[i]:Q[i]+1]:
            V[i] = 3
        else:
            V[i] = 4
    return V