def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        if budget < money:
            break
        else:
            budget -= money
            answer += 1
    
    return answer