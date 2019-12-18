def solution(x, n):
    answer = []
    value = 0
    while len(answer) < n:
        value += x
        answer.append(value)
    return answer


# List Comprehension
def solution(x, n):
    return [x*i for i in range(1, n+1)]