"""
[참고사이트]
https://greenapple16.tistory.com/89

규칙을 참고하여 풀음

왜 gcd가 이용되어 해결되는지 파악필요
"""

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(w, h):
    answer = w*h - (w + h - gcd(w, h))
    return answer
