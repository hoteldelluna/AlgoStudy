# 프로그래머스
# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버

'''

숫자 리스트로 더하거나 뺀 숫자들의 트리 구조 만들기

참고: https://codedrive.tistory.com/50

'''

def solution(numbers, target):
    box = [0]
    for i in numbers:
        temp = []
        for j in box:
            temp.append(j+i)
            temp.append(j-i)
        box = temp
    ans = box.count(target)
    return ans


numbers = [1, 1, 1, 1, 1]
target = 3
# ans = 5

res = solution(numbers, target)
print(res)