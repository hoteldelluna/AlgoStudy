def solution(s):
    answer = False
    check = [0,0]
    for alpha in s:
        if alpha.lower() == 'p':
            check[0] += 1
        elif alpha.lower() == 'y':
            check[1] += 1
    
    if check[0] == check[1]:
        answer = True

    return answer

"""
count를 사용하여 간략화할수 있다.
"""
def solution(s):
    return s.lower().count('p') == s.lower().count('y')