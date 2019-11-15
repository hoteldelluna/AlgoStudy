"""
시간초과를 생각해야하는 문제
import sys로 입력 부분을 빠르게 하여야 시간초과를 해결할 수 있다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
DP = [0] * (N+1)

for i in range(1, len(arr)+1):
    DP[i] = DP[i-1] + arr[i-1]
for _ in range(M):
    start, end = map(int, input().split())
    print(DP[end] - DP[start-1])