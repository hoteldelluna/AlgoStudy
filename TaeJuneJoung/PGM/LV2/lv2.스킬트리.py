def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        stack = []
        for tree in skill_tree:
            if tree in set(skill):
                idx = skill.index(tree)
                if idx not in set(stack):
                    stack.append(idx)
        
        isPlus = True
        check = [False] * len(skill)
        for i in stack:
            check[i] = True
            if check[:i].count(False):
                isPlus = False
                break
                
        if isPlus:
            answer += 1
            
    return answer

"""
다른 사람 풀이]
Python의 `for~else`문 사용
"""
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer