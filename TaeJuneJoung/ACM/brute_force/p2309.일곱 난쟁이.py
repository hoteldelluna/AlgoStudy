"""
[완전탐색_조합]
정답이 여러가지인 경우 정답 중 아무거나 출력
"""

def nCr(n, r):
    if r == 0:
        if sum(box) == 100:
            box.sort()
            for i in range(7):
                res[i] = box[i]
        return
    elif n < r:
        return
    else:
        box[r-1] = arr[n-1]
        nCr(n-1, r-1)
        nCr(n-1, r)

arr = [int(input()) for i in range(9)]
box = [0] * 7
res = [0] * 7
nCr(9, 7)
for i in range(7):
    print(res[i])