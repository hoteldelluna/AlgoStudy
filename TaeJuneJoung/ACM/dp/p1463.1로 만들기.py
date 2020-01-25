"""
다른 사람 소스를 참고하여 풀음
"""

X = int(input())

dp = [-1] * (X+1)

for i in range(1, X+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[X])