# 백준 N과 M(3) 15651번 문제

# 입력: N, M (1 <= M =< N <= 7)
# 출력: 1부터 N까지 길이가 M인 수열 구하기(중복 O)

'''
중복이 가능하다 = 방문표시를 할 필요가 없다.
'''

N, M = map(int, input().split())

res = [0]*M
arr = [_ for _ in range(1, N+1)]

def f(n, k, m):
    if n == k:
        print(*res)
        return

    for i in range(m):
        res[n] = arr[i]
        f(n+1, k, m)

f(0, M, N)