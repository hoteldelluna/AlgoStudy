"""
[완주하지 못한 선수]
효율성 문제
"""

def solution(participant, completion):
    participant.sort(); completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

"""
다른 사람 풀이
"""
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]