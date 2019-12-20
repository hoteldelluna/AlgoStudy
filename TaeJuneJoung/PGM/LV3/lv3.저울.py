"""
[저울]
당연히 부분집합의 합으로 풀면 되겠다 하였는데...시간초과
찾아보니 아래와 같은 방도로 풀면 해결됨...
"""

def solution(weight):
    weight.sort()
    answer = 1
    for i in range(len(weight)):
        if answer < weight[i]:
            return answer
        answer += weight[i]
    return answer