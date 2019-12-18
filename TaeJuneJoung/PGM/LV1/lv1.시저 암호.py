"""
[시저 암호]
ord로 확인 결과
A: 65 Z:90
a: 97 z: 122
"""

def solution(s, n):
    answer = ''
    for value in s:
        if value != ' ':
            if ord(value) < 91:
                if ord(value) + n > 90:
                    answer += chr(ord(value) + n - 26)
                else:
                    answer += chr(ord(value) + n)
            else:
                if ord(value) + n > 122:
                    answer += chr(ord(value) + n - 26)
                else:
                    answer += chr(ord(value) + n)
        else:
            answer += ' '
    return answer

"""
ord(value) 대소문자 구분을 isupper()와 islower()로 처리할 수 있음
"""