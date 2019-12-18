def solution(n):
    answer = '수박' * (n//2) + ('수' if n%2 else '')
    return answer