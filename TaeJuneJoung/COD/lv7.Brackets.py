"""
맨마지막 괄호가 먼저 닫혀야 다음 괄호를 처리할 수 있기에
괄호들을 stack에 넣고 짝이 맞으면 계속 이어가고,
짝이 틀리다면 return 0

신경써야 하는 부분
1. 짝은 맞는데 여는 괄호가 닫는 괄호보다 많을 때
2. stack에 있는 길이보다 닫는 괄호가 더 나와 에러가 발생할 때
"""

def solution(S):
    stack = []
    open_str = "{[("
    close_str = "}])"
    for char in S:
        if char == '{':
            val = 0
            stack.append(val)
        elif char == '[':
            val = 1
            stack.append(val)
        elif char == '(':
            val = 2
            stack.append(val)
        if char == '}':
            try:
                current = stack.pop(-1)
            except IndexError:
                return 0
            if current != 0:
                return 0
        elif char == ']':
            try:
                current = stack.pop(-1)
            except IndexError:
                return 0
            if current != 1:
                return 0
        elif char == ')':
            try:
                current = stack.pop(-1)
            except IndexError:
                return 0
            if current != 2:
                return 0
    
    if len(stack):
        return 0

    return 1