"""
p와 x의 같은 순서들을 곱해서 해당 값들을 다 더해주면 해결. 
"""

T = int(input())
for t in range(1, T+1):
    N = int(input())
    res = 0
    for i in range(N):
        p, x = map(float, input().split())
        res += p * x
    print("#{} {}".format(t, res))