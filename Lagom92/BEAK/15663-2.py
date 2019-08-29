# N과 M (9) 15663번 문제

'''
입력:
N, M
N개의 수

출력:
N개의 자연수 중에서 M개의 수열(수열이 중복 X)

'''


def f(n, m, k):
    if n == k:
        print(res)
        result.append(res)
        return

    for i in range(m):
        if not used[i]:
            used[i] = 1
            res[n] = arr[i]
            f(n+1, m, k)
            used[i] = 0

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))

used = [0]*N
res = [0]*M

result = []
f(0, N, M)
print(result)