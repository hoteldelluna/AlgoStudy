"""
[K번째수]
"""

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        value = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(value[commands[i][2]-1])
    return answer


"""
다른 사람 풀이
- lambda를 이용한 한줄 풀이
"""

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))