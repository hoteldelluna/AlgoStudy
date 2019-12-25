"""
[파도반 수열]
규칙을 찾아보니
P(n) = P(n-1) + P(n-5)

N은 1이상 100이하라고 하니 모두 구해놓는다.
SW Expert Academy p.3376.파도반 수열과 동일 문제
"""

T = int(input())
arr = [0,1,1,1,2]
arr[5:101] = [0] * (101 -5)

for i in range(5, 101):
    arr[i] = arr[i-1] + arr[i-5]

for t in range(1, T+1):
    N = int(input())
    print(arr[N])
