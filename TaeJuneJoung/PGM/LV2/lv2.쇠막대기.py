def solution(arrangement):
    answer = 0
    stack = [arrangement[0]]
    before = arrangement[0]
    for i in range(1,len(arrangement)):
        if arrangement[i] == '(':
            if arrangement[i] == before: #before (
                stack.append(arrangement[i])
            else: #before )
                # ) (
                stack.append(arrangement[i])
        else: #)
            if arrangement[i] == before: #before )
                #)) 막대 끝
                stack.pop()
                answer += 1
            else: #before (
                #() 레이저
                stack.pop()
                answer += len(stack)
                
        before = arrangement[i]
                
    return answer