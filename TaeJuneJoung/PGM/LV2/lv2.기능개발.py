import math

def solution(progresses, speeds):
    answer = []
    access = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]
    before = 0
    for i in range(len(access)):
        if access[before] < access[i]:
            answer.append(i-before)
            before = i
    answer.append(len(access)-before)
    return answer