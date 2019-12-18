def solution(n):
    num = n**0.5
    if num - int(num):
        answer = -1
    else:
        answer = (num+1)**2
    return answer
