def solution(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return 0
            value = stack.pop()
    if stack:
        return 0
    return 1