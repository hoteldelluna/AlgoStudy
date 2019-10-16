# Codility
# 1. BinaryGap 문제

'''
주어진 숫자를 2로 나누다가
나머지가 1일때부터 다시 1이 나올때 까지
카운트를 하는 방식으로 문제를 풀었다.

리스트를 만들어서 최대를 구하지 않고
if를 추가하여 최대값을 구할 수도 있을거 같다.
'''

def solution(N):
    cnts = []
    cnt = 0
    flag = False
    while N > 0:
        if N % 2:
            N = N // 2
            flag = True
            cnts.append(cnt)
            cnt = 0

        else:
            N = N // 2
            if flag:
                cnt += 1

    return max(cnts)