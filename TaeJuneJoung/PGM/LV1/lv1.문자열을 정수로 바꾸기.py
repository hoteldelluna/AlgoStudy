def solution(s):
    if s[0].isdigit():
        answer = int(s)
    else:
        if s[0] == '+':
            answer = int(s[1:])
        else:
            answer = -1*int(s[1:])

    return answer