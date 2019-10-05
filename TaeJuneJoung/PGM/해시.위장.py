"""
규칙을 찾아보면 쉬운 문제
의상의 종류가 있는데
해당 된 것은 하나가 사용될 수도 있고,
다른 의상의 종류에서 더해 사용할 수 있다.
(단, 같은 의상에서 더 사용은 안된다)

예를 들어.
(얼굴+1) * (상의+1) * (하의+1) * (겉옷+1) -1 = 문제의 모든 경우의 수

다른 사람 풀이 참조:
https://programmers.co.kr/learn/courses/30/lessons/42578/solution_groups?language=python3
"""

def solution(clothes):
    kind = dict()
    item = set()
    for cloth in clothes:
        if cloth[1] in kind:
            if not (cloth[0] in item):
                kind[cloth[1]] += 1
        else:
            item.add(cloth[0])
            kind[cloth[1]] = 1
    
    answer = 1
    for val in kind.values():
        answer *= (val+1)

    return answer-1