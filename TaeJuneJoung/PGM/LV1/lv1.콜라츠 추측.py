def solution(num):
    answer = 0
    if num == 1: #13번 테스트케이스 Pass를 위해
        return 0
    while answer < 500:
        answer += 1
        if num%2:#홀수
            num = num * 3 +1
        else: #짝수
            num = num // 2
        if num == 1:
            break
    return answer if answer < 500 else -1