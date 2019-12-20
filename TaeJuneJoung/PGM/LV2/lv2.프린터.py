"""
[프린터] - 다른 사람 소스 보고 풀음
"""

def solution(priorities, location):
    answer = 0
    maxV = max(priorities)
    while True:
        value = priorities.pop(0)
        if maxV == value:
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
            maxV = max(priorities)
        else:
            priorities.append(value)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer