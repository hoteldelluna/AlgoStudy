def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor == 0:
            answer.append(num)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer

"""
List Comprehension으로 더 간단하게 구현 가능
"""
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor ==0]
    return sorted(answer) if len(answer) != 0 else [-1]