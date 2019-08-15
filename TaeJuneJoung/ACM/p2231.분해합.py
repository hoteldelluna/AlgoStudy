"""
[완전탐색]
내용을 이해하면 쉽다
각 자리를 더한 값 중에 가장 작은 수를 구하는 것인데
완전탐색으로 1~N까지 그러한 경우를 검색하다가
처음 나오는 경우가 가장 작은 수이니 값을 내어주면 된다.
없는 경우에 0을 내놓아야한다는 점도 잊어서는 안된다.
"""

N = int(input())
res = 0
for i in range(1, N+1):
    sum_num = 0
    for j in str(i):
        sum_num += int(j)
    if (sum_num + i) == N:
        res = i
        break
print(res)