#  SW Expert Academy 5189번 문제
# [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

'''
순열 문제 인것 같다.
시간 테이블의 행에서 하나식 빼서 더해봐서 최소값과 비교를 계속 다 하면 될거같다.
시작은 1번부터!
'''

# 전기 카트
T = int(input())

def f(n, k, s):
    global minV

    if n == N:
        s += arr[k][0]
        if minV > s:
            minV = s
        return
    elif s >= minV:
        return
    else:
        for i in range(1, N):
            if used[i] == 0:
                used[i] = 1
                f(n+1, i, s + arr[k][i])
                used[i] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*(N+1)
    used[0] = 1
    minV = 10000

    f(1, 0, 0)

    print("#{} {}".format(tc, minV))