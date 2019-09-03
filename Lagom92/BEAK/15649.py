# 백준 N과 M(1) 15649번 문제

# 입력: N, M
# 출력: 1부터 N까지 길이가 M인 수열 구하기(중복 X)

def f(k, n, m):
    if k == m:
        print(*res)
        return    
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                res[k] = arr[i]
                f(k+1, n, m)
                used[i] = 0

N, M = map(int, input().split())
arr = [ _ for _ in range(1, N+1)]
res = [0]*M
used=[0]*N

f(0, N, M)