# SW Expert 1952번 문제
# 모의 SW 역량테스트 수영장

'''
각 달 마다 가능한 상황 다 구하기
재귀 이용
'''

T = int(input())
def f(n, s):
    global minV
    if n >= 12:
        if s < minV:
            minV = s
            return
    elif minV <= s:
        return
    else:
        f(n+1, s + plans[n]*expense[0])
        f(n+1, s + expense[1])
        f(n+3, s + expense[2])

for tc in range(1, T+1):
    expense = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    minV = expense[3]
    f(0, 0)
    print("#{} {}".format(tc, minV))