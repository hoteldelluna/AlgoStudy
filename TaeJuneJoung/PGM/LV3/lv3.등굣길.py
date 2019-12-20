"""
집과 학교가 물에 빠지는 경우는 없다고 하였는데
편리성을 위해 index가 0부터 시작하는게 아닌,
1부터 시작하였더니 집 위치는 넘어가라고 처리해줘야 했다.

격자가 100이 넘어가서 효율성을 생각한다면 DP로 풀어야 하는 문제로 판단하여
경로의 수를 짜는 코드를 작성하였고, 물 웅덩이가 있기에 조합을 이용한 수식으로 풀 순 없다 판단

참고하면 좋을 사이트(참고하여 풀진 않음)
https://blog.naver.com/PostView.nhn?blogId=parkhc1992&logNo=220669287080&proxyReferer=https%3A%2F%2Fwww.google.com%2F
"""

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[-1][-1]