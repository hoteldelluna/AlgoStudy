# Codility
# Lesson 7 Brackets

'''
( ) , { } 와 [ ] 가 정상적으로 있는지 체크
정상이면 1
비정상이면 0 출력

여는 괄호만 box에 넣고 닫는 괄호가 나오면 box의 맨 뒤 부터 
값을 가져와서 비교함

비정상인 부분이 발생하면 return 발생
'''

def solution(S):
    box = list()
    openText = '({['
    closeText = ')}]'

    for s in S:
        if s in closeText:
            if box:
                text = box.pop()
                if text == openText[0]:
                    if s != closeText[0]:
                        return 0
                elif text == openText[1]:
                    if s != closeText[1]:
                        return 0
                else:
                    if s != closeText[2]:
                        return 0
            else:
                return 0
        else:
            box.append(s)
            
    # for문을 다 돌았는데 box에 남은게 있으면 비정상        
    return 0 if box else 1      

S = "{[()("
res = solution(S)
print(res)