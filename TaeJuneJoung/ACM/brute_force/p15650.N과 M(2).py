"""
[완전탐색_순열]
k : 현재 숫자 위치
n : 총 리스트의 길이
r : 뽑아야할 리스트의 길이
b : 이전 값 -> sort역할을 하기 위해
"""
def nCr(k, n, r, b):
    if k == r:
        print(*res)
        return
    else:
        for i in range(n):
            if arr[i] > b:
                b = res[k] = arr[i]
                nCr(k+1, n, r, b)

n, r = map(int, input().split())
arr = range(1, n+1)
res = [0] * r
b = 0
nCr(0, n, r, b)