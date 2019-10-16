# SW Expert
# 2115. [모의 SW 역량테스트] 벌꿀채취

'''
같은 줄에서 두 일꾼이 벌꿀을 채취하는것은 안된다

검사하는 비트가 0이면 연산 결과가 0

일꾼이 2인것을 기억!

각 줄마다 최대를 구한후 그 최대값들의 리스트(res)들중 최대값 2개를 골라 합하면 끝 !

'''

# 비트연산 - 부분집합
def f(m, c, arr):
    global maxV
    for i in range(1, 2**m):    # 1 ~ 2**M-1까지 2진수 생성
        s = 0
        ss = 0
        for j in range(m):
            if i & (1<<j) != 0 and s+arr[j] <= c:
                s += arr[j]
                ss += arr[j]**2
        if maxV < ss:
            maxV = ss
    return

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    res = [0, 0]

    for i in range(N):
        maxV = 0
        for j in range(N-M+1):
            box = []
            for k in range(M):
                arr = board[i][j+k]
                box.append(arr)
            f(M, C, box)
        res.append(maxV)

    res = sorted(res, reverse=True)
    result = res[0] + res[1]
    print("#{} {}".format(tc, result))