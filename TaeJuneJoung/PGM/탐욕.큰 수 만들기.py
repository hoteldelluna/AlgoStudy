"""
앞에서부터 판별하면서
제거 갯수(k)가 존재하면 뒷값보다 작을 경우
앞에값들 제거하고 뒷값을 담는 방식
"""

def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        if k == 0:
            stack.append(number[i:])
            break
        else:
            stack.append(number[i])
    stack = stack[:len(number)-k] if k > 0 else stack
    answer = ''.join(stack)
    return answer


# 다른 사람 방법
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)