# 백준 N과 M(2) 15650번 문제

# 입력: N, M (1 <= M =< N <= 8)
# 출력: 1부터 N까지 길이가 M인 수열 구하기(중복 X, 오름차순)


N, M = map(int, input().split())

res = [0]*M
used = [0]*N
arr = [_ for _ in range(1, N+1)]
def f(n, k, m, be):
    if n == k:
        print(*res)
        return
    else:
        for i in range(m):
            if used[i] == 0 and arr[i] > be:
                used[i] = 1
                be = arr[i]
                res[n] = arr[i]
                f(n+1, k, m, be)
                used[i] = 0

f(0, M, N, 0)

