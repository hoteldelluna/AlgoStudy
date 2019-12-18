def solution(x):
    sumV = sum(map(int, str(x)))
    answer = False if x%sumV else True
    return answer