def solution(answers):
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    values = [0,0,0]
    for i in range(len(answers)):
        if person1[i%len(person1)] == answers[i]:
            values[0] += 1
        if person2[i%len(person2)] == answers[i]:
            values[1] += 1
        if person3[i%len(person3)] == answers[i]:
            values[2] += 1
    answer = []
    maxV = max(values)
    for i in range(len(values)):
        if values[i] == maxV:
            answer.append(i+1)
    return answer