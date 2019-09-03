# N과 M (9) 15663번 문제

'''
입력:
N, M
N개의 수

출력:
N개의 자연수 중에서 M개의 수열(수열이 중복 X)

'''

'''
가장 먼저 생각한 코드, 값은 나오는것 같은데..
그런데 시간초과가 발생했다...
python3로 실행했을때는 시간초과가 발생 단 pypy3로 실행하면 통과됬다.

15663-2.py 에서 코드를 다시 작성
'''
def f(n, m, k):
    global result
    if n == k:
        w = ""
        for i in res:
            w += str(i) + " "
        if w not in result:
            result.append(w)
        return
    else:
        for i in range(m):
            if used[i] == 0:
                used[i] = 1
                res[n] = arr[i]
                f(n+1, m, k)
                used[i] = 0

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))

res = [0]*M
used = [0]*len(arr)

result = []
f(0, N, M)
for i in result:
    print (i)




