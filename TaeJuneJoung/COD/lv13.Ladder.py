"""
피보나치수열
A에 들어오는 수는 피보나치 수열에 인덱스를 나타내고
B에 들어오는 수는 2**B[i]를 통해
A의 값을 `%`해야하는 역할을 한다.
여기서 퍼포먼스를 고려한다면
B의 범위가 2^30이 최대이기에 fibo 범위는 50000이므로,
최대값에 나머지값을 넣어줌으로서 연산의 크기를 줄여 시간을 줄여야한다.
"""

def solution(A, B):
    fibo = [0]*50001
    fibo[0] = 1
    fibo[1] = 1
    maxV = 2 ** 30
    for i in range(2, len(A)+1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % maxV

    answer = [0] * len(A)
    for i in range(len(A)):
        answer[i] = fibo[A[i]] % (2**B[i])
        
    return answer