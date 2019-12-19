def solution(s):
    stack = []
    if s.count('(') != s.count(')'):
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True