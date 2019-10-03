"""
Codility는 문제풀이보다 문제를 이해하는게 더 어려울 때가 많다...
문제 Title인 Distinct를 보면 알수 있듯,
중복값을 지워서 리스트의 길이를 나타내면 된다.
"""

def solution(A):
    return len(set(A))