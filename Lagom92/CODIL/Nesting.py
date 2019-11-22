# Codility
# Lesson 7 Nesting
'''
Brackets 문제와 매우 유사하다.

'''

def solution(S):
    box = []
    for s in S:
        if s == '(':
            box.append(s)
        else:
            if box:
                del box[0]
            else:
                return 0
    return 0 if box else 1 


S = '(())'
res = solution(S)
print(res)