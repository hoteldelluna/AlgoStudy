def solution(strings, n):
    return sorted(strings, key=lambda i: (i[n], i))