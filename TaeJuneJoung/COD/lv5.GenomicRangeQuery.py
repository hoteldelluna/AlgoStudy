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