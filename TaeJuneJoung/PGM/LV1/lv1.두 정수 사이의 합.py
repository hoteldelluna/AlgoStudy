"""
[두 정수 사이의 합]
"""

def solution(a, b):
    answer = 0
    b, a = (a, b) if a > b else (b, a)
    for i in range(a, b+1): #answer = sum(range(a, b+1))로 처리 가능
        answer += i
    return answer

"""
등차수열의 합 공식을 이용하면 쉽게 해결할 수 있음
a = 초기값
b = a+nd
Sn = a + (a+d) + (a+2d) + ... + (a+nd)
위의 식을 아래와 같이 쓸수도 있다.
Sn = a + (a+d) + (a+2d) + ... + (b-d) + b ... 1
Sn = b + (b-d) + ... + (a+2d) + (a+d) + a ... 2
1번과 2번식을 더하면
2Sn = (a+b) * n
Sn = (a+b)*n / 2
여기서 n은 갯수이므로 b-a+1개이다.(b>=a일때)

참고 사이트: https://mathbang.net/609
"""

def solution(a, b):
    return (abs(b-a)+1) * (b+a) // 2
