"""
[재귀함수 공부하기 좋은 문제]
http://pythontutor.com/visualize.html#mode=edit
위의 주소 참고하여 디버깅하면 Good
"""

def f(E):
    sumV = 0
    if len(E) == N-2:
        return 0
    for i in range(1, len(E)-1):
        maxV = E[i-1] * E[i+1]
        nextE = E[:i] + E[i+1:]
        maxV += f(nextE)
        if sumV < maxV:
            sumV = maxV
    return sumV

N = int(input())
E = list(map(int, input().split()))
print(f(E))