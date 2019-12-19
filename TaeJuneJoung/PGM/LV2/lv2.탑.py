def solution(heights):
    answer = []
    top = [(i+1, heights[i]) for i in range(len(heights))]
    
    for i in range(len(top)-1, -1, -1):
        isOk = True
        for j in range(i-1, -1, -1):
            if top[i][1] < top[j][1]:
                answer.append(top[j][0])
                isOk = False
                break
        if isOk:
            answer.append(0)
    return list(reversed(answer))


"""
다른 사람 풀이
"""

def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans