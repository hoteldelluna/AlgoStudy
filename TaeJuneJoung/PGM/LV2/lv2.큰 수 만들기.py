"""
오랜만에 짰으나 당연히 시간초과...
"""

def solution(number, k):
    maxV = 0
    box_size = len(number) - k
    box = [0] * box_size
    visited = [0] * len(number)
    def nPr(n, r, idx):
        nonlocal maxV
        if r == 0:
            value = int(''.join(box))
            maxV = value if maxV < value else maxV
        else:
            for i in range(len(number)):
                if i >= idx and visited[i] == 0:
                    visited[i] = 1
                    idx = i
                    box[box_size-r] = number[i]
                    nPr(n, r-1, idx)
                    visited[i] = 0
    nPr(len(number), box_size, 0)
    answer = maxV
    return str(answer)

"""
아래와 같이 짜면 통과
기존에 처리되지 않는 number 길이가 1일때 k가 1이면 0이 나오게도 처리함
"""
def solution(number, k):
    if len(number) == k:
        return '0'
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:len(number)-k])