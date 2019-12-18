"""
[이상한 문자 만들기]
split을 썼을 때 안되는 것을 보니
앞에 부분이나 중간 부분에 ' '인 white space가 들어간 Test Case들이 있는 것 같다.
"""

def solution(s):
    answer = ''
    cnt = 0
    for value in s:
        if value == ' ':
            cnt = -1
        if cnt % 2:
            answer += value.lower()
        else:
            answer += value.upper()
        cnt += 1
    return answer