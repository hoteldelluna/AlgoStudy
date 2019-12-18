def solution(s):
    lenS = len(s)
    if lenS % 2: #홀수
        answer = s[lenS//2]
    else: #짝수
        answer = s[lenS//2-1:lenS//2+1]
    return answer