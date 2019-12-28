"""
[H-index]
다른 사람 소스를 참조하여 풀음
"""

def solution(citations):
    size = len(citations)
    for idx, value in enumerate(sorted(citations)):
        if value >= size - idx:
            return size - idx
    return 0


"""
아래와 같은 방도도 신박함
"""

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer