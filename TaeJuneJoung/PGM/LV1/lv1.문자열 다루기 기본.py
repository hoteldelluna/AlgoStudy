"""
[문자열 다루기 기본]
"""

def solution(s):
    try:
        answer = int(s)
        if len(s) == 4 or len(s) == 6:
            answer = True
        else:
            answer = False
    except ValueError:
        answer = False
    return answer

"""
다른 사람의 풀이
"""
def solution(s):
    return s.isdigit() and len(s) in (4, 6)


# 정규화 방식
import re
def solution(s):
    return bool(re.match('^(\d{4}|\d{6})$', s))