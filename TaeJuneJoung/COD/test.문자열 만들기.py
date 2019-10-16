"""
[Problem]
A라는 문장이 주어질 때, 주어진 문장 요소들로
CODILITY를 몇 번 만들 수 있는지 return 하시오.
(단, 사용한 요소는 다시 재사용할 수 없습니다.)
"""

def solution(A):
    """
    C 1개 / O 1개 / D 1개 / I 2개 / L 1개 / T 1개 / Y 1개
    하나의 CODILITY를 만들기 위해서는 위와 같은 갯수가 필요하다.
    box : 해당 문자의 수를 담을 리스트
    CODILTY : 해당 문자를 만들기 위한 최소 갯수를 담는 리스트

    1. 문자열의 문자들을 for문과 if문을 통해 살펴본다.
     - 딕셔너리를 사용해도 되지만, 하드코딩은 퍼포먼스에서는 좋을 수 있기에...
    2. 1번에서 확인된 내용 중 사용해야할 문자가 있다면 처리한 index에 +1
     - CODILTY에서 인덱스는 각 문자의 순서와 같다
    3. 문자열을 돌며 만들어진 box를 이용하여 최소갯수와 비교해보며,
    최소로 가지고 있는 문자열의 갯수만큼이 만들 수 있는 문자열의 수이다.
    """
    box = [0] * 7
    CODILTY = [1, 1, 1, 2, 1, 1, 1]
    for a in A:
        if a == 'C':
            box[0] += 1
        elif a == 'O':
            box[1] += 1
        elif a == 'D':
            box[2] += 1
        elif a == 'I':
            box[3] += 1
        elif a == 'L':
            box[4] += 1
        elif a == 'T':
            box[5] += 1
        elif a == 'Y':
            box[6] += 1
    
    minV = box[0] // CODILTY[0]
    for i in range(1, len(box)):
        minV = min(minV, box[i] // CODILTY[i])
    
    return minV
