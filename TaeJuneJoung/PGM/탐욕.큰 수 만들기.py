"""
테스트 8, 10 시간초과
테스트 12 실패

수정할 것
"""

def solution(number, k):
    stack = []
    for i in range(len(number)):
        for j in range(len(stack)-1, -1, -1):
            if k > 0 and int(stack[j]) < int(number[i]):
                stack.pop()
                k -= 1

        stack.append(number[i])
        if k ==0:
            stack.append(number[i+1:])
            break
    answer = ''.join(stack)
    return answer