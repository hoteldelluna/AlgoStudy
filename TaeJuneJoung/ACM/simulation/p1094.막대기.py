"""
[시뮬레이션]
막대기의 길이가 64이고 반절로 자르는 작업
X의 길이는 자연수이며 64보다 작기에,
64부터 1로 `내림차순`으로 보면 해결
"""

sticks = [64, 32, 16, 8, 4, 2, 1]
X = int(input())

cnt = 0
X_current = X
for stick in sticks:
    if X_current >= stick:
        X_current -= stick
        cnt += 1
print(cnt)