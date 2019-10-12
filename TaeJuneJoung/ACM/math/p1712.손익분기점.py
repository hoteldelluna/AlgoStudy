"""
손익분기점
A: 고정비용
B: 가변 비용
C: 판매 수익

A + B*x < C*x 이므로,
A < (C-B)x
-> x > A//(C-B)
"""

A, B, C = map(int ,input().split())

if C-B > 0:
    print(A//(C-B) +1)
else: #손익 분기점을 넘지 못하는 경우
    print(-1)