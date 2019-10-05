"""
이름순으로 나열한 후,
무조건 한명이 완주하지 못하였다 하였으니
다른 값이 나오면 Return

다른 사람 풀이 참조:
https://programmers.co.kr/learn/courses/30/lessons/42576/solution_groups?language=python3
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(completion)-1
    for p in range(len(participant)-1, -1, -1):
        if participant[p] == completion[n]:
            n -= 1
        else:
            return participant[p]