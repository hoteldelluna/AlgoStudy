"""
[소수 찾기]
기존 방식으로 하다간 효율성에서 통과하지 못함
그래서 아리스토텔레스 체를 사용하기로 결정
"""

def solution(n):
    visited = [0] * (n+1) #0, 1 은 빼줘야함
    for i in range(2, n+1):
        j = 2
        while i*j <= n:
            if visited[i*j] == 0:
                visited[i*j] = 1
            j += 1
    answer = visited.count(0) - 2
    return answer


# 아래 코드는 기존 방식
def solution(n):
    answer = 0
    for i in range(2, n+1):
        isPre = True
        for j in range(2, i//2 +1):
            if i%j == 0:
                print(i, j)
                isPre = False
                break
        if isPre:
            answer += 1
    return answer


#다른 사람의 아리스토텔레스 체
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)