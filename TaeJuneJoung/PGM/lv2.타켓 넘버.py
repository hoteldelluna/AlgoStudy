"""
[DFS/BFS] - LEVEL2
global과 nonlocal에 대한 개념 이해 필요
"""

def solution(numbers, target):
    answer = 0
    len_nums = len(numbers)
    def oper(idx=0): #idx -> default=0
        if idx < len_nums:
            oper(idx+1)
            
            numbers[idx] *= -1
            oper(idx+1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    oper()
    return answer