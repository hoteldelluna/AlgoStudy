"""
스티커를 자르는데 하나를 짜르면 양쪽을 사용하지 못한다
스티커를 이용해서 가장 크게 만들 수 있는 숫자를 return하시오.
예1)
[12, 12, 12, 12, 12]
>> 36

예2)
[12, 20, 40, 100, 40]
>> 120

예3)
[12, 20, 40, 20, 100, 16]
>> 152

스티커의 갯수는 최대 100,000,000장이다.
"""

def soluction(S):
    N = len(S)
    DP = [0] * N
    DP[0] = S[0]
    DP[1] = S[1]
    step2, step3 = 0, 0
    for i in range(2, N):
        if i >= 2:
            step2 = S[i] + DP[i-2]
        if i >= 3:
            step3 = S[i] + DP[i-3]

        DP[i] = max(step2, step3)
    
    return max(DP[-1], DP[-2])